from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @staticmethod
    def xml_convert_to_dict(file):
        tree = ET.parse(file)
        root = tree.getroot()
        file_data = []
        for item in root:
            new_item = {}
            for item_data in item:
                new_item[item_data.tag] = item_data.text
            file_data.append(new_item)
        return file_data

    @classmethod
    def read_csv_file(cls, path):
        with open(path) as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file))
            elif path.endswith(".json"):
                return json.load(file)
            elif path.endswith(".xml"):
                return cls.xml_convert_to_dict(file)
            else:
                return None

    @classmethod
    def import_data(cls, path, report_type):
        data = cls.read_csv_file(path)
        if (report_type == "simples"):
            return SimpleReport.generate(data)
        elif (report_type == "completo"):
            return CompleteReport.generate(data)
        return None
