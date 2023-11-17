# Generated by Django 4.2.7 on 2023-11-13 04:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="earthquake",
            old_name="location",
            new_name="coordinates",
        ),
        migrations.RemoveField(
            model_name="earthquake",
            name="name",
        ),
        migrations.RemoveField(
            model_name="earthquake",
            name="street_name",
        ),
        migrations.RemoveField(
            model_name="seismicintensity",
            name="name",
        ),
        migrations.AddField(
            model_name="earthquake",
            name="location_name",
            field=models.CharField(default="", max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name="earthquake",
            name="mmi",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="seismicintensity",
            name="mmi",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="seismicintensity",
            name="scale_level",
            field=models.CharField(default="", max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name="seismicintensity",
            name="description",
            field=models.TextField(default=""),
        ),
    ]
