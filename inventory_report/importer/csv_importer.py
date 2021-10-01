import csv
from .importer import Importer


class CsvImporter(Importer):
    def import_data(file_name):
        if 'csv' in file_name:
            with open(file_name) as csv_file:
                data = csv.DictReader(csv_file)
                new_data = [row for row in data]
                return new_data
        else:
            raise ValueError("Arquivo inválido")
    pass
