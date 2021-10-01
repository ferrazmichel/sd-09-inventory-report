import json
from .importer import Importer


class JsonImporter(Importer):
    def import_data(file_name):
        if 'json' in file_name:
            with open(file_name) as json_file:
                data = json.load(json_file)
                new_data = [row for row in data]
                return new_data
        else:
            raise ValueError("Arquivo inválido")
    pass
