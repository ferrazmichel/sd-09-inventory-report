from abc import ABC, abstractclassmethod


class Importer(ABC):

    """metodo abstrato"""
    @abstractclassmethod
    def import_data(path):
        pass
