# Generated by Django 4.2.2 on 2023-08-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_subscription_day_alter_subscription_month_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_video_publisher',
        ),
        migrations.RemoveField(
            model_name='user',
            name='language',
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس اینستاگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='telegram',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس تلگرام'),
        ),
        migrations.AddField(
            model_name='user',
            name='whatsapp',
            field=models.URLField(blank=True, null=True, verbose_name='آدرس واتساپ'),
        ),
        migrations.DeleteModel(
            name='SelectedSubscription',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
