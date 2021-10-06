from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    def import_data(fileName):
        extension = fileName.split(".")[-1]
        if extension != "csv":
            raise ValueError("Arquivo inválido")
        else:
            with open(fileName) as file:
                return list(csv.DictReader(file, delimiter=","))
