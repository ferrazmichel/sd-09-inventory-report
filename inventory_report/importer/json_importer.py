import json
from importer import Importer


class JsonImporter(Importer):
    def __init__(self, file_name):
        self.file_name = file_name

    def import_json(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)
