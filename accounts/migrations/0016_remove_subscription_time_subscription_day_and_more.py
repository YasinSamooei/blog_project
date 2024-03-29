# Generated by Django 4.2.2 on 2023-08-13 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0015_alter_subscription_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="time",
        ),
        migrations.AddField(
            model_name="subscription",
            name="day",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="مدت زمان(روزانه)"
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="month",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="مدت زمان(ماهانه)"
            ),
        ),
        migrations.AddField(
            model_name="subscription",
            name="week",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="مدت زمان(هفتگی)"
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="new_films",
            field=models.BooleanField(
                default=False, verbose_name="دسترسی به قسمت  جدید"
            ),
        ),
    ]
