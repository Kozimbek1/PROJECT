# Generated by Django 5.0.5 on 2024-05-09 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
