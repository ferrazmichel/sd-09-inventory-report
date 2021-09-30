from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith("csv"):
            with open(path, "r") as file:
                file_list = list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                )
                # print(file_list)
                return file_list
        else:
            raise ValueError("Arquivo inválido")
