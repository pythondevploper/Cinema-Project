# Generated by Django 5.0.1 on 2024-05-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movierecapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieclub",
            name="description",
            field=models.CharField(max_length=1000),
        ),
    ]
