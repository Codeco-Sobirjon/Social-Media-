# Generated by Django 5.0.6 on 2024-08-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_fcmtoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='message',
            new_name='body',
        ),
        migrations.AddField(
            model_name='notification',
            name='title',
            field=models.CharField(default='Test notification', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('follow', 'Follow'), ('content', 'Content')], default='content', max_length=10),
            preserve_default=False,
        ),
    ]