from inventory_report.importer.importer import Importer
import xmltodict

# https://python-guide-pt-br.readthedocs.io/pt_BR/latest/scenarios/xml.html
# pip install xmltodict


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith("xml"):
            with open(path, "r") as file:
                file_list = xmltodict.parse(file.read())["dataset"]["record"]
                # print(file_list)
                return file_list
        else:
            raise ValueError("Arquivo inválido")
