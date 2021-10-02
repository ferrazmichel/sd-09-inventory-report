from xml.etree.ElementTree import XMLID
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


# class CompleteReport(SimpleReport, Manage_list):
#     """gerador de relatorio - herdada da classe SimpleReport"""
#     def generate(list):
#         result_simple_report = SimpleReport.generate(list)
#         result_manage_list = Manage_list.count_stock(list, 1)

#         """monta a segunda parte da string para retorno"""
#         companies_rows = ''
#         for key, value in result_manage_list.items():
#             companies_rows += '- {}: {}\n'.format(key, value)

#         return (
#             '{}\n'
#             'Produtos estocados por empresa: \n'
#             '{}'
#             .format(result_simple_report, companies_rows)
#         )

from functools import lru_cache
from csv import DictReader
import json
from xml.etree import ElementTree
import os.path
# path_csv = 'inventory_report/data/inventory.json'


# class Inventory(SimpleReport, CompleteReport):
class Inventory(CompleteReport, SimpleReport):

    @lru_cache
    def import_data_csv(path):
        with open(path, 'r', encoding='utf8') as file:
            spam_reader = DictReader(file)
            read_list = [rows for rows in spam_reader]
            return read_list

    @lru_cache
    def import_data_json(path):
        with open(path) as file:
            json_reader = json.load(file)
            read_list = [rows for rows in json_reader]
            return read_list

    @lru_cache
    def import_data_xml(path):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        read_list = []
        for elem in root:
            items = {}
            for subelem in elem:
                items[subelem.tag] = subelem.text
                # print(subelem.text)
            read_list.append(items)
        return read_list

    def import_data(path, option):
        extension = os.path.splitext(path)[1]

        if(extension == '.csv'):
            list = Inventory.import_data_csv(path)
        elif(extension == '.json'):
            list = Inventory.import_data_json(path)
        elif(extension == '.xml'):
            list = Inventory.import_data_xml(path)
        else:
            raise ValueError('Arquivo inválido')

        if(option == 'simples'):
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)


# print(Inventory.import_data(path_csv, 'complete'))
