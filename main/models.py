from django.db import models
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


class TypeOfService(models.Model):
    img = ResizedImageField(
        size=[800, 600],
        crop=["middle", "center"],
        upload_to="objects/",
        verbose_name="Изображение",
        null=True,
        blank=True,
        quality=90,
    )
    name = models.CharField("Название", max_length=150)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Master(models.Model):
    POSITION_CHOICES = [
        ("top_master", "Top Master"),
        ("master", "Master"),
        ("trainee", "Trainee"),
    ]

    img = ResizedImageField(
        size=[800, 600],
        crop=["middle", "center"],
        upload_to="objects/",
        verbose_name="Изображение",
        null=True,
        blank=True,
        quality=90,
    )
    name = models.CharField("Название", max_length=150)
    position = models.CharField("Позиция", max_length=20, choices=POSITION_CHOICES, default="master")
    experience = models.IntegerField("Опыт")
    description = models.TextField("Описание", max_length=1500)
    telegramm = models.URLField("Телеграм", null=True, blank=True)
    instagram = models.URLField("Инстаграм", null=True, blank=True)
    tiktok = models.URLField("TikTok", null=True, blank=True)
    whatsapp = models.URLField("WhatsApp", null=True, blank=True)
    youtube = models.URLField("YouTube", null=True, blank=True)
    type = models.ForeignKey(TypeOfService, on_delete=models.CASCADE, verbose_name="Тип сервиса")

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Gallery(models.Model):
    img = ResizedImageField(
        size=[800, 600],
        crop=["middle", "center"],
        upload_to="objects/",
        verbose_name="Изображение",
        null=True,
        blank=True,
        quality=90,
    )
    name = models.CharField("Название", max_length=150)
    type = models.ForeignKey(TypeOfService, on_delete=models.CASCADE, verbose_name="Тип сервиса")

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"


class Service(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    price = models.PositiveIntegerField("Цена")
    masters = models.ManyToManyField(Master, verbose_name="Мастера", related_name="services")
    type = models.ForeignKey(TypeOfService, on_delete=models.CASCADE, verbose_name="Тип сервиса", related_name="services")

    def __str__(self):
        return f"{self.id} - {self.title}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Review(models.Model):
    SCORE_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер", related_name="reviews")
    score = models.IntegerField("Оценка", choices=SCORE_CHOICES, default=1)
    comment = models.TextField("Комментарий", max_length=1500, blank=True)

    def __str__(self):
        return f"{self.id} - Оценка мастера {self.master.name}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class SignUp(models.Model):
    name = models.CharField("Имя", max_length=150)
    phone_number = PhoneNumberField("Номер телефона")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга", related_name="signups")
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Мастер", related_name="signups")
    date = models.DateField("Дата")
    time = models.TimeField("Время")
    comment = models.TextField("Комментарий", max_length=1500, blank=True)

    def __str__(self):
        return f"{self.id} - Запись {self.name}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
