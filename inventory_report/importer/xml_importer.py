from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def import_data(fileName):
        extension = fileName.split(".")[-1]
        if extension != "xml":
            raise ValueError("Arquivo inválido")
        else:
            root = ET.parse(fileName).getroot()
            read_list = []
            for element in root:
                items = {}
                for subelem in element:
                    items[subelem.tag] = subelem.text
                read_list.append(items)
            return read_list
