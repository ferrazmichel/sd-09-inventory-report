from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer

from functools import lru_cache
import os.path


class CsvImporter(Importer, Inventory):

    """testa se a opção selecionada foi para xml"""
    @lru_cache
    def import_data(path):
        extension = os.path.splitext(path)[1]
        if(extension == '.csv'):
            list = Inventory.valid_files(path)
            return list
        else:
            raise ValueError('Arquivo inválido')
