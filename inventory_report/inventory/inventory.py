import csv
import json
from xml.etree import ElementTree
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class ReportFile:
    def __init__(self, path):
        self.path = path

    def get_csv(self):
        with open(self.path) as file:
            products = csv.DictReader(file)
            products_list = []
            for product in products:
                products_list.append(product)
        return products_list

    def get_json(self):
        with open(self.path) as file:
            products_list = json.load(file)
        return products_list

    def get_xml(self):
        # Auxlío do Rafa Reis e Leo
        # site: https://www.geeksforgeeks.org/reading-and-writing-xml
        # -files-in-python/#:~:text=To%20read%20an%20XML%20file,xml%20file%20using%20getroot().
        tree = ElementTree.parse(self.path)
        root = tree.getroot()

        products_list = []
        for element in root:
            product = {}
            for obj in element:
                product[obj.tag] = obj.text
            products_list.append(product)
        return products_list


class Inventory:
    @classmethod
    def import_data(cls, path, type_report):
        report_file = ReportFile(path)

        if path.endswith('.csv'):
            products_list = report_file.get_csv()
        elif path.endswith('.json'):
            products_list = report_file.get_json()
        elif path.endswith('.xml'):
            products_list = report_file.get_xml()

        if type_report == 'simples':
            return SimpleReport.generate(products_list)
        return CompleteReport.generate(products_list)


Inventory.import_data('inventory_report/data/inventory.csv', 'simples')
