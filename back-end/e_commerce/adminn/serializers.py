from rest_framework import serializers
from .models import CarImage, Cars, CarThumbnail

class CreateItemSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True
    )
    available = serializers.CharField(default=True)
    class Meta:
        model = Cars
        exclude = ['publish_date']
    def create(self, validated_data):
        images = validated_data.pop('images')
        fuel_type = validated_data.get("fuel_type").capitalize()
        condition = validated_data.get("condition").capitalize()
        transmission = validated_data.get("transmission").capitalize()
        description = validated_data.get("description").capitalize()
        category = validated_data.get("category").capitalize()
        brand = validated_data.get('brand').capitalize()
        car_model = validated_data.get("car_model").capitalize()
        price =  validated_data.get("price")
        car = Cars.objects.create(
            fuel_type=fuel_type, 
            condition=condition, 
            transmission=transmission,
            description=description,
            category=category,
            car_model=car_model,
            price=price,
            brand=brand
        )
        CarThumbnail.objects.create(car=car, image=images[0])
        for image in images:
            CarImage.objects.create(car=car, image=image)
        return car