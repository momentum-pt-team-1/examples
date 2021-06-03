import requests

from django.core.management.base import BaseCommand

from garden.models import Plant


class Command(BaseCommand):
    help = 'create plants from API data'

    def handle(self, *args, **kwargs):
        data = requests.get('https://plants.ces.ncsu.edu/api/plants/').json().get('results')
        for plant in data:
            if len(plant.get('commonname_set')) > 0:
                common_name = plant.get('commonname_set')[0]
            else:
                common_name = ''
            scientific_name = plant.get('scientific_name')

            new_plant = Plant.objects.create(common_name=common_name, scientific_name=scientific_name)
