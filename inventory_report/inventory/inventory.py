from csv import DictReader

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:

    def import_data(path, type_report):
        type = {
            "simples": SimpleReport.generate,
            "completo": CompleteReport.generate,
        }

        with open(path, 'r') as file:
            read_file = list(DictReader(file, delimiter=','))
            file_report = type[type_report](read_file)
            return file_report
