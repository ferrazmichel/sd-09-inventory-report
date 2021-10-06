from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        extension = path.split(".")[-1]
        if extension != 'csv':
            raise TypeError
        with open(path, mode='r') as file:
            return list(csv.DictReader(file))
