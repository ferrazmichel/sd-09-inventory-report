from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith("json"):
            with open(path, "r") as file:
                file_list = list(json.load(file))
                # print(file_list)
                return file_list
        else:
            raise ValueError("Arquivo inválido")
