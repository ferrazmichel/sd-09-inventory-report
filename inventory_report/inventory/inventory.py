from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from csv import DictReader

import xml.etree.ElementTree as ET
import json


class Inventory:
    def _read_csv(file, extension):
        if extension != "csv":
            print("Type error")

        else:
            return list(DictReader(file, delimiter=","))

    def _read_json(file, extension):
        if extension != "json":
            print("Type erro")
        else:
            return json.load(file)

    def _read_xml(path, extension):
        if extension != "xml":
            print("Type erro")

        else:
            root = ET.parse(path).getroot()
            read_list = []
            for element in root:
                items = {}
                for subelem in element:
                    items[subelem.tag] = subelem.text
                read_list.append(items)
            return read_list

    @classmethod
    def import_data(cls, path, type_report):
        type_generate = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }
        extension = path.split(".")[-1]
        with open(path, "r") as file:
            print("==============", extension)
            type_file = {
                "csv": cls._read_csv(file, extension),
                "json": cls._read_json(file, extension),
                "xml": cls._read_xml(path, extension),
            }

            read_file = type_file[extension]
            print("==============", read_file)
            file_report = type_generate[type_report](read_file)
            print("==============", file_report)
            return file_report
