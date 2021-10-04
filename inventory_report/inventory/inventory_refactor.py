from _collections_abc import Iterable
from .inventory_iterator import InventoryIterator


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, file_path, type_report):
        new_data = self.importer.import_data(file_path)
        if len(new_data):
            self.data += new_data
            return
        self.data.append(new_data[0])

    def __iter__(self):

        return InventoryIterator(self.data)
