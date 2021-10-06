from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    def import_data(fileName):
        extension = fileName.split(".")[-1]
        if extension != "json":
            raise ValueError("Arquivo inválido")
        else:
            with open(fileName) as file:
                return json.load(file)
