from django.db import models


class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class House(models.Model):
    house_id = models.AutoField(primary_key=True)
    property_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
