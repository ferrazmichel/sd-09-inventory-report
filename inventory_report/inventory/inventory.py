from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def verify_extension(cls, path):
        if path.endswith('.csv'):
            with open(path, 'r') as file:
                products = csv.DictReader(file, delimiter=",", quotechar='"')
                products_list = [product for product in products]
            return products_list
        elif path.endswith('.json'):
            with open(path, 'r') as file:
                return json.load(file)
        elif path.endswith('.xml'):
            with open(path, 'r') as file:
                products = xmltodict.parse(file.read())
                products_list = [
                  dict(product)
                  for product in products["dataset"]["record"]
                ]
                return products_list

    @classmethod
    def import_data(cls, path, type_report):
        data_list = cls.verify_extension(path)
        if type_report == "simples":
            return SimpleReport.generate(data_list)
        elif type_report == "completo":
            return CompleteReport.generate(data_list)
