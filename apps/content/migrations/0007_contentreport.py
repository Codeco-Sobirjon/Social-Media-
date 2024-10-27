# Generated by Django 5.0.6 on 2024-09-01 08:49

import config.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_alter_content_media_aspect_ratio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentReport',
            fields=[
                ('id', config.utils.CustomAutoField(editable=False, primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=512, null=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='content.content')),
            ],
            options={
                'verbose_name': 'Content report',
                'verbose_name_plural': 'Content reports',
                'db_table': 'content_reports',
            },
        ),
    ]