import csv
import os
from datetime import datetime

from api import models
from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned
from django.core.management.base import BaseCommand, CommandError


def data_extraction(f):
    file_path = os.path.join(getattr(settings, "BASE_DIR"), f)
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        skip_first_row = True
        for row in csv_reader:
            if skip_first_row:
                skip_first_row = False
                continue
            yield row


class Command(BaseCommand):
    help = "Import existing data to the application."

    def add_arguments(self, parser):
        parser.add_argument("files", nargs="+", type=str)

    def handle(self, *args, **options):
        """
        Iterates through each file, line by line, and converts each line
        into record in the application.
        """
        for f in options.get("files"):
            for l in data_extraction(f):
                self.line_to_records(l)
            self.stdout.write(self.style.SUCCESS(f"Successfully imported {f}!"))

    def contextualize(self, line):
        """
        This is our contract or schema, ideally this would be a _struct_
        or some other data structure to contextualize and convert the data.
        """
        return {
            "area_unit": str(line[0]),
            "bathrooms": float(line[1]) if line[1] else None,
            "bedrooms": float(line[2]) if line[2] else None,
            "home_size": int(line[3]) if line[3] else None,
            "home_type": str(line[4]),
            "last_sold_date": datetime.strptime(line[5], "%m/%d/%Y").date()
            if line[5]
            else None,
            "last_sold_price": int(line[6]) if line[6] else None,
            "link": str(line[7]),
            "price": str(line[8]),
            "property_size": int(line[9]) if line[9] else None,
            "rent_price": int(line[10]) if line[10] else None,
            "rentzestimate_amount": int(line[11]) if line[11] else None,
            "rentzestimate_last_updated": datetime.strptime(line[12], "%m/%d/%Y").date()
            if line[12]
            else None,
            "tax_value": float(line[13]) if line[13] else None,
            "tax_year": int(line[14]) if line[14] else None,
            "year_built": int(line[15]) if line[15] else None,
            "zestimate_amount": int(line[16]) if line[16] else None,
            "zestimate_last_updated": datetime.strptime(line[17], "%m/%d/%Y").date()
            if line[17]
            else None,
            "zillow_id": int(line[18]),
            "address": str(line[19]),
            "city": str(line[20]),
            "state": str(line[21]),
            "zipcode": int(line[22]),
        }

    def get_or_create(self, model, **data):
        """
        Passing a dict of fields that are not in a given model
        raises a FieldError. We want to keep the code succinct as
        possible, so we check if the field exists before we interact
        with the model object.
        """
        return model.objects.get_or_create(
            **{
                k: v
                for k, v in data.items()
                if k in [field.name for field in model._meta.fields]
            }
        )

    def line_to_records(self, line):
        try:
            data = self.contextualize(line)
            zillow, _ = self.get_or_create(models.Zillow, id=data["zillow_id"], **data)
            location, _ = self.get_or_create(models.Location, **data)
            evaluation, _ = self.get_or_create(models.Evaluation, **data)
            property_detail, _ = self.get_or_create(models.PropertyDetail, **data)
            data["zillow_id"] = zillow
            self.get_or_create(
                models.Property,
                location_id=location,
                evaluation_id=evaluation,
                detail_id=property_detail,
                **data,
            )
        except (TypeError, ValueError) as err:
            raise CommandError(f"Abort. {err} {line}")
        except MultipleObjectsReturned:
            raise CommandError(
                f"Abort. Multiple records found while processing: {line}"
            )
