from rest_framework import serializers
from django.conf import settings
from main.models import Service, Master, Gallery, Review, TypeOfService, SignUp
from datetime import datetime
from django.utils import timezone


class TypeOfServiceSerializers(serializers.ModelSerializer):
    class Meta:    
        model = TypeOfService
        fields = ('img', 'name',)


class MasterSerializers(serializers.ModelSerializer):
    class Meta:    
        model = Master
        fields = ('img', 'name', 'position', 'experience', 'description',
                'telegramm', 'instagram', 'tiktok', 'whatsapp', 'youtube', 'type',)
        

class GallerySerializers(serializers.ModelSerializer):
    class Meta:    
        model = Gallery
        fields = ('img', 'name',)


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:    
        model = Review
        fields = ('master', 'score', 'comment',)

    def validate_score(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError('Оценка долна быть от 1 до 5!')
        return value
        
    def validate_comment(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError('Комментарий слишком короткий!')
        return value

    
class ServiceSerializers(serializers.ModelSerializer):
    class Meta:    
        model = Service
        fields = ('title', 'price', 'masters', 'type')

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Цена должна быть больше 0!')
        return value


class SignUpSerializers(serializers.ModelSerializer):
    class Meta:    
        model = SignUp
        fields = ('name', 'phone_number', 'service', 'master',
                'date', 'time', 'comment',)

    def validate(self, attrs):
        booking_dt = datetime.combine(attrs["date"], attrs["time"])

        booking_dt = timezone.make_aware(booking_dt, timezone.get_current_timezone())

        now = timezone.now()

        if booking_dt < now:
            raise serializers.ValidationError("Нельзя записаться в прошлое")

        exists = SignUp.objects.filter(
            master=attrs["master"],
            date=attrs["date"],
            time=attrs["time"],
        ).exists()

        if exists:
            raise serializers.ValidationError("Мастер уже занят на это время")

        return attrs