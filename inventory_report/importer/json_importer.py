from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        extension = path.split('.')[-1]
        if extension != 'json':
            raise ValueError('Arquivo inválido')
        else:
            with open(path, mode='r') as file:
                return json.load(file)
