from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict
import json
import csv


class Inventory:
    @classmethod
    def files_path(cls, path):
        extension = path.split(".")[-1]
        with open(path, mode="r") as file:
            if extension == "xml":
                file_list = xmltodict.parse(file.read())["dataset"]["record"]
                result = [dict(order) for order in file_list]
                return result
            elif extension == "json":
                return json.load(file)
            elif extension == "csv":
                return list(csv.DictReader(file))
            else:
                return None

    @classmethod
    def import_data(cls, path, type):
        inventory = cls.files_path(path)
        if type == "simples":
            return SimpleReport.generate(inventory)
        if type == "completo":
            return CompleteReport.generate(inventory)
