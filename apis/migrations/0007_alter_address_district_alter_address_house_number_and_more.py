# Generated by Django 4.1.7 on 2023-02-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0006_alter_user_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="district",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="house_number",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="province",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="road",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="sub_district",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="village",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="address",
            name="zip_code",
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
