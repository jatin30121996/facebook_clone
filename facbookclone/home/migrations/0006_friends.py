# Generated by Django 4.2.14 on 2024-08-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_friendrequest"),
    ]

    operations = [
        migrations.CreateModel(
            name="Friends",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("friend", models.CharField(max_length=100)),
            ],
        ),
    ]
