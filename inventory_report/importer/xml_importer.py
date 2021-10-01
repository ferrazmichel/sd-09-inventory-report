from .importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(file_name):
        if 'xml' in file_name:
            with open(file_name) as file:
                data = ET.parse(file)
                itemlist = data.getroot()
                complete_list = []
                for item in itemlist:
                    items = {}
                    for it in item:
                        items[it.tag] = it.text
                    complete_list.append(items)
            return complete_list
        else:
            raise ValueError("Arquivo inválido")
    pass
