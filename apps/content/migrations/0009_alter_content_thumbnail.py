# Generated by Django 5.1.1 on 2024-09-08 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_content_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='contents/'),
        ),
    ]