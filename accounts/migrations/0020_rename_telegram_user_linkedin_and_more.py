# Generated by Django 4.2.2 on 2023-08-15 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "accounts",
            "0019_alter_otp_options_alter_user_options_alter_otp_code_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="telegram",
            new_name="linkedin",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="whatsapp",
            new_name="twitter",
        ),
    ]
