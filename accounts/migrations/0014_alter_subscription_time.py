# Generated by Django 4.2.2 on 2023-08-12 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0013_alter_subscription_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="time",
            field=models.TimeField(blank=True, null=True, verbose_name="مدت زمان"),
        ),
    ]
