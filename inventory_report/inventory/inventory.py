import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(csvList, type_report):
        with open(csvList) as file:
            empresas = csv.DictReader(file, delimiter=",", quotechar='"')
            if type_report == "simples":
                return SimpleReport.generate(empresas)
            if type_report == "completo":
                return CompleteReport.generate(empresas)


print(
    Inventory.import_data(
        'inventory_report/data/inventory.csv', "completo"))
