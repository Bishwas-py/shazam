# Generated by Django 4.1.2 on 2022-10-20 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Shazam Blog", max_length=100)),
                (
                    "description",
                    models.TextField(
                        default="A blog developed with Django and SvelteKit"
                    ),
                ),
                ("author", models.CharField(default="Bishwas-py", max_length=100)),
                ("domain", models.CharField(default="shazam.blog", max_length=100)),
                (
                    "url",
                    models.CharField(default="https://shazam.blog", max_length=100),
                ),
                ("email", models.CharField(default="", max_length=100)),
            ],
        ),
    ]