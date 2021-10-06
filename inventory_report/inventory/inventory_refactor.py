from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, path):
        extension = path.split('.')[-1]
        if extension == 'json':
            self.importer = JsonImporter
        elif extension == 'xml':
            self.importer = XmlImporter
        elif extension == 'csv':
            self.importer = CsvImporter

    def import_data(cls, path, type):
        inventory = cls.importer(path)
        if type == "simples":
            return SimpleReport.generate(inventory)
        if type == "completo":
            return CompleteReport.generate(inventory)

    def __iter__(self):
        return InventoryIterator(self.data)
