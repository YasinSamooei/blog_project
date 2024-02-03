# Generated by Django 4.2.2 on 2023-08-15 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0018_remove_user_gender_remove_user_is_video_publisher_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="otp",
            options={},
        ),
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AlterField(
            model_name="otp",
            name="code",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="otp",
            name="email",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="otp",
            name="expiration",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="otp",
            name="full_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="otp",
            name="password",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="otp",
            name="token",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="bio",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="full_name",
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name="user",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/users"),
        ),
        migrations.AlterField(
            model_name="user",
            name="instagram",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="telegram",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="whatsapp",
            field=models.URLField(blank=True, null=True),
        ),
    ]
