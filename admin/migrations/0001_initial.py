# Generated by Django 5.1.2 on 2024-12-29 04:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fuel_type', models.CharField(max_length=20)),
                ('condition', models.CharField(max_length=5)),
                ('millage', models.PositiveIntegerField()),
                ('transmission', models.CharField(max_length=20)),
                ('first_registration', models.CharField(default='Not registered', max_length=255)),
                ('engine_power', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('interior_material', models.CharField(max_length=255)),
                ('chases_id', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('available', models.CharField(default='Yes', max_length=3)),
                ('car_model', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('drive_type', models.PositiveIntegerField()),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Cars',
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='admin.cars')),
            ],
            options={
                'db_table': 'car_image',
            },
        ),
        migrations.CreateModel(
            name='CarThumbnail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_thumbnail')),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='admin.cars')),
            ],
            options={
                'db_table': 'car_thumbnail',
            },
        ),
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='media/profile_picture/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile_picture',
            },
        ),
    ]
