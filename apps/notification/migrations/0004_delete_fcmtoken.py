# Generated by Django 5.0.6 on 2024-08-09 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_rename_message_notification_body_notification_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FCMToken',
        ),
    ]