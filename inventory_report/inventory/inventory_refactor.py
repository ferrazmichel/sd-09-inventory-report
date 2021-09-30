from _collections_abc import Iterable
from .inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, type_report):
        self.data += self.importer.import_data(path)
        if type_report == "simples":
            return SimpleReport.generate(self.data)
        elif type_report == "completo":
            return CompleteReport.generate(self.data)
