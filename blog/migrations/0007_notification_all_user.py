# Generated by Django 4.2.2 on 2023-08-15 12:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0006_alter_blog_options_alter_comment_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="notification",
            name="all_user",
            field=models.ManyToManyField(
                related_name="users", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
