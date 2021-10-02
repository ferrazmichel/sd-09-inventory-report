from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer

from functools import lru_cache
import os.path


path_list = 'inventory_report/data/inventory.json'


class JsonImporter(Importer, Inventory):

    """testa se a opção selecionada foi para xml"""
    @lru_cache
    def import_data(path):
        extension = os.path.splitext(path)[1]
        if(extension == '.json'):
            list = Inventory.valid_files(path)
            return list
        else:
            raise ValueError('Arquivo inválido')
