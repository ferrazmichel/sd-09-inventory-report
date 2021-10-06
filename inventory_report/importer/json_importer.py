import importer
import json


class JsonImporter(importer):
    @classmethod
    def import_data(cls, path):
        extension = path.split('.')[-1]
        if extension != 'json':
            raise TypeError
        with open(path, mode='r') as file:
            return json.load(file)
