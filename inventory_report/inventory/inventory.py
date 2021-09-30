from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    def import_data(path, type):
        if path.endswith("csv"):
            with open(path, "r") as file:
                file_list = list(
                    csv.DictReader(file, delimiter=",", quotechar='"')
                )
                # print(file_list)

        elif path.endswith("json"):
            with open(path, "r") as file:
                file_list = list(json.load(file))
                # print(file_list)

        elif path.endswith("xml"):
            with open(path, "r") as file:
                file_list = xmltodict.parse(file.read())["dataset"]["record"]
                # print(file_list)
        if type == "simples":
            return SimpleReport.generate(file_list)
        else:
            return CompleteReport.generate(file_list)
