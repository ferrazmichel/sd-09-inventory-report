from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_path):
        type_check = file_path.lower().endswith('.csv')
        if not type_check:
            raise ValueError("Arquivo inválido")
        else:
            return Inventory.get_data_by_file_type(file_path)

