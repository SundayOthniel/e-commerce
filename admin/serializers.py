from .models import CarImage, Cars, CarThumbnail
from .utility import image_thumbnail_upload, car_images
from cloudinary.exceptions import Error as CloudinaryError
from rest_framework import serializers

class CreateItemSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        max_length=5
    )
    
    class Meta:
        model = Cars
        exclude = ['publish_date']
    def create(self, validated_data):
        images = validated_data.pop('images')
        
        fuel_type = validated_data.get("fuel_type").capitalize()
        # condition = validated_data.get("condition").capitalize()
        # millage = validated_data.get("millage")
        # transmission = validated_data.get("transmission").capitalize()
        # first_registration = validated_data.get("first_registration").capitalize()
        # engine_power = validated_data.get("engine_power")
        # description = validated_data.get("description").capitalize()
        # interior_material = validated_data.get("interior_material").capitalize()
        # chases_id = validated_data.get("chases_id")
        # category = validated_data.get("category").capitalize()
        # brand = validated_data.get('brand').capitalize()
        # car_model = validated_data.get("car_model").capitalize()
        # drive_type = validated_data.get("drive_type")
        # price =  validated_data.get("price")
        
        car = Cars.objects.create(
            fuel_type=fuel_type, 
            # condition=condition, 
            # transmission=transmission,
            # first_registration=first_registration,
            # engine_power=engine_power,
            # interior_material=interior_material,
            # chases_id=chases_id,
            # drive_type=drive_type,
            # description=description,
            # category=category,
            # car_model=car_model,
            # price=price,
            # brand=brand,
            # millage=millage
        )
        
        if images:
            # try:
                thumbnail_upload = image_thumbnail_upload(images)
                CarThumbnail.objects.create(car=car, image=thumbnail_upload['secure_url'])
                
                for image in images:
                    image_upload = car_images(image)
                    CarImage.objects.create(car=car, image=image_upload['secure_url'])
            # except CloudinaryError as e:
            #     raise serializers.ValidationError(f"Image upload failed: {str(e)}")
            
        return car