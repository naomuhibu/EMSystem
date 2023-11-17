# Generated by Django 4.2.7 on 2023-11-13 04:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0002_rename_location_earthquake_coordinates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="earthquake",
            name="location_name",
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="earthquake",
            name="mmi",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="seismicintensity",
            name="description",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="seismicintensity",
            name="mmi",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="seismicintensity",
            name="scale_level",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
