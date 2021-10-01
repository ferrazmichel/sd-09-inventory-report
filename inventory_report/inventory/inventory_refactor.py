import sys
sys.path.append("../")

from reports.complete_report import CompleteReport
from reports.simple_report import SimpleReport
from importer.json_importer import JsonImporter
from importer.csv_importer import CsvImporter
from importer.xml_importer import XmlImporter
from inventory_iterator import InventoryIterator

# from ..reports.complete_report import CompleteReport
# from ..reports.simple_report import SimpleReport
# from ..importer.json_importer import JsonImporter
# from ..importer.csv_importer import CsvImporter
# from ..importer.xml_importer import XmlImporter
# from .inventory_iterator import InventoryIterator


def report_type(type_report, new_data):
    if type_report == "simples":
        return SimpleReport.generate(new_data)
    if type_report == "completo":
        return CompleteReport.generate(new_data)


class InventoryRefactor:
    def __init__(self, importer):

        self.importer = importer
        self.data = []

    def import_data(self, file_path, type_report):

        new_data = self.importer.import_data(file_path)

        # result = report_type(type_report, new_data)
        self.data.append(new_data)

        return self.data

    def __iter__(self):
        return InventoryIterator(self.data)


instance = InventoryRefactor(CsvImporter)
instance.import_data("../data/inventory.csv", "simples")
iterator = iter(instance)
first_item_instance = next(iterator)
print(first_item_instance)