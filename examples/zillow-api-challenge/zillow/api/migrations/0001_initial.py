# Generated by Django 2.1.5 on 2019-01-26 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evaluation",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("last_sold_date", models.DateTimeField(blank=True, null=True)),
                ("last_sold_price", models.IntegerField(blank=True, null=True)),
                ("price", models.TextField()),
                ("rent_price", models.IntegerField(blank=True, null=True)),
                ("tax_value", models.FloatField(blank=True, null=True)),
                ("tax_year", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("city", models.TextField()),
                ("state", models.TextField()),
                ("zipcode", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("address", models.TextField()),
                ("area_unit", models.TextField()),
                ("bathrooms", models.FloatField(blank=True, null=True)),
                ("bedrooms", models.FloatField(blank=True, null=True)),
                ("home_size", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="PropertyDetail",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("home_type", models.TextField()),
                ("property_size", models.IntegerField(blank=True, null=True)),
                ("year_built", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Zillow",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("link", models.TextField()),
                ("rentzestimate_amount", models.IntegerField(blank=True, null=True)),
                (
                    "rentzestimate_last_updated",
                    models.DateTimeField(blank=True, null=True),
                ),
                ("zestimate_amount", models.IntegerField(blank=True, null=True)),
                ("zestimate_last_updated", models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="property",
            name="detail_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="api.PropertyDetail",
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="evaluation_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="api.Evaluation",
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="location_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="api.Location",
            ),
        ),
        migrations.AddField(
            model_name="property",
            name="zillow_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="api.Zillow",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="location", unique_together={("city", "state", "zipcode")}
        ),
    ]
