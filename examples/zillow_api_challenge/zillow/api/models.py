from django.db import models


class Zillow(models.Model):
    id = models.AutoField(primary_key=True)
    link = models.TextField()
    rentzestimate_amount = models.IntegerField(null=True, blank=True)
    rentzestimate_last_updated = models.DateTimeField(null=True, blank=True)
    zestimate_amount = models.IntegerField(null=True, blank=True)
    zestimate_last_updated = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {self.link}"


class Evaluation(models.Model):
    id = models.AutoField(primary_key=True)
    last_sold_date = models.DateTimeField(null=True, blank=True)
    last_sold_price = models.IntegerField(null=True, blank=True)
    price = models.TextField()
    rent_price = models.IntegerField(null=True, blank=True)
    tax_value = models.FloatField(null=True, blank=True)
    tax_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class PropertyDetail(models.Model):
    id = models.AutoField(primary_key=True)
    home_type = models.TextField()
    property_size = models.IntegerField(null=True, blank=True)
    year_built = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}"


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.TextField()
    state = models.TextField()
    zipcode = models.IntegerField()

    def __str__(self):
        return f"{self.city}, {self.state}, {self.zipcode}"

    class Meta:
        # This _might_ by deprecated in the future.
        unique_together = ("city", "state", "zipcode")


class Property(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.TextField()
    area_unit = models.TextField()
    bathrooms = models.FloatField(null=True, blank=True)
    bedrooms = models.FloatField(null=True, blank=True)
    evaluation_id = models.ForeignKey(
        Evaluation, on_delete=models.CASCADE, related_name="+"
    )
    home_size = models.IntegerField(null=True, blank=True)
    location_id = models.ForeignKey(
        Location, on_delete=models.SET_NULL, blank=True, null=True, related_name="+"
    )
    detail_id = models.ForeignKey(
        PropertyDetail, on_delete=models.CASCADE, related_name="+"
    )
    zillow_id = models.ForeignKey(Zillow, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.address}"
