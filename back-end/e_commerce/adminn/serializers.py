from rest_framework import serializers
from .models import CarImage, Cars

class CreateItemSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )
    
    class Meta:
        model = Cars
        exclude = ['publish_date']
    def create(self, validated_data):
        images = validated_data.pop('images') 
        car = Cars.objects.create(**validated_data)
        for image in images:
            CarImage.objects.create(car=car, image=image)
        return car