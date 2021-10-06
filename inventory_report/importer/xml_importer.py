from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        extension = path.split('.')[-1]
        if extension != 'xml':
            raise TypeError
        with open(path, mode='r') as file:
            file_list = xmltodict.parse(file.read())["dataset"]["record"]
            result = [dict(order) for order in file_list]
            return result
