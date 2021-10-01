# import sys
# sys.path.append("../")
# from reports.complete_report import CompleteReport
# from reports.simple_report import SimpleReport

import json
import csv
import xml.etree.ElementTree as ET

from ..reports.complete_report import CompleteReport
from ..reports.simple_report import SimpleReport


def read_csv(file_path):
    with open(file_path) as file:
        data = csv.DictReader(file)
        new_data = [row for row in data]
        print(new_data)
        return new_data


def read_json(file_path):
    with open(file_path) as file:
        data = json.load(file)
        new_data = [row for row in data]
        return new_data


def read_xml(file_path):
    with open(file_path) as file:
        data = ET.parse(file)
        itemlist = data.getroot()

        complete_list = []
        for item in itemlist:
            items = {}
            for it in item:
                items[it.tag] = it.text
            complete_list.append(items)

        return complete_list


def report_type(type_report, new_data):
    if type_report == "simples":
        return SimpleReport.generate(new_data)
    if type_report == "completo":
        return CompleteReport.generate(new_data)


class Inventory:
    def import_data(file_path, type_report):
        if "csv" in file_path:
            new_data = read_csv(file_path)

        if "json" in file_path:
            new_data = read_json(file_path)

        if "xml" in file_path:
            new_data = read_xml(file_path)

        return report_type(type_report, new_data)

    pass
