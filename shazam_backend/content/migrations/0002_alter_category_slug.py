# Generated by Django 4.1.2 on 2022-10-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
