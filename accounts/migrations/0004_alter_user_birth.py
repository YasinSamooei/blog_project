# Generated by Django 4.2.2 on 2023-07-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="تاریخ تولد"
            ),
        ),
    ]
