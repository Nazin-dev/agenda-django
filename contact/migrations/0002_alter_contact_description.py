# Generated by Django 5.1.6 on 2025-03-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, max_length=254),
        ),
    ]
