import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        with open(path) as file:
            products = csv.DictReader(file)
            products_list = []
            for product in products:
                products_list.append(product)
        if type_report == 'simples':
            return SimpleReport.generate(products_list)
        return CompleteReport.generate(products_list)
