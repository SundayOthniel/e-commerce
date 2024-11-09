from rest_framework import serializers
from .models import CarImage, Car

class CreateItemSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )
    available = serializers.CharField(default=True)
    class Meta:
        model = Car
        exclude = ['publish_date']
    def create(self, validated_data):
        images = validated_data.pop('images') 
        car = Car.objects.create(**validated_data)
        for image in images:
            CarImage.objects.create(car=car, image=image)
        return car