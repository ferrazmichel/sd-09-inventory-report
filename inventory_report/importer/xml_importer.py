import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    def import_data(path):
        with open(path) as file:
            if path.endswith(".xml"):
                tree = ET.parse(file)
                root = tree.getroot()
                file_data = []
                for item in root:
                    new_item = {}
                    for item_data in item:
                        new_item[item_data.tag] = item_data.text
                    file_data.append(new_item)
                return file_data
            raise ValueError("Arquivo inválido")
