# Generated by Django 4.2.14 on 2024-08-02 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_loginto"),
    ]

    operations = [
        migrations.AddField(
            model_name="loginto",
            name="gender",
            field=models.CharField(default="", max_length=20),
        ),
    ]
