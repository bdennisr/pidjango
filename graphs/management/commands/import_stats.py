from django.core.management.base import BaseCommand
from graphs.models import spindelData
import json


class Command(BaseCommand):
    help = 'Import bite exercise stats'

    def add_arguments(self, parser):
        parser.add_argument('-f', '--file', required=True)

    def handle(self, *args, **options):
        file = options["file"]
        with open(file) as f:
            data_dict = json.load(f)
        
        data_list = data_dict['data']
        for data in data_list:
            stat, created = spindelData.objects.get_or_create(
                name = data['name'],
                spindle_id = data['ID'],
                token = data['token'],
                gravity_unit = data['gravity-unit'],
                temp_units = data['temp_units'],
                interval = data['interval'],
                temperature = data['temperature'],
                gravity = data['gravity'],
                angle =data['angle'],
                battery = data['battery'],
                RSSI = data['RSSI'],
                corr_gravity = data['corr-gravity'],
                run_time = data['run-time']
            )

            if created:
                self.stdout.write(f"{stat} created")
            else:
                self.stderr.write(f"{stat} already in db")