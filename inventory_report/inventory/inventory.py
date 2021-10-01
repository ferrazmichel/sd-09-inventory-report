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


path_csv = 'inventory_report/data/inventory.csv'


# class Inventory(SimpleReport, CompleteReport):
class Inventory(CompleteReport, SimpleReport):

    @lru_cache
    def import_data(path, option):
        with open(path, 'r', encoding='utf8') as csvfile:
            spamreader = DictReader(csvfile)
            list = [rows for rows in spamreader]

        if(option == 'simples'):
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)



# print(Inventory.import_data(path_csv, 'simples'))
