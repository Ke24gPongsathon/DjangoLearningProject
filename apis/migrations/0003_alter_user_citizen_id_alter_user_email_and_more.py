# Generated by Django 4.1.7 on 2023-02-23 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0002_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="citizen_id",
            field=models.CharField(max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(default="", max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.IntegerField(choices=[(1, "male"), (2, "female")], default=1),
        ),
    ]
