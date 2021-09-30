import csv
import json
import pathlib
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @classmethod
    def __read_file(cls, file_path):
        with open(file_path) as file:
            file_extension = pathlib.Path(file_path).suffix
            if file_extension == '.csv':
                return list(csv.DictReader(file))
            if file_extension == '.json':
                return json.load(file)
            if file_extension == '.xml':
                # TODO -> READ XML FILE
                return False

    @classmethod
    def import_data(cls, file_path, report_type):
        data = cls.__read_file(file_path)
        if report_type == 'simples':
            return SimpleReport.generate(data)
        if report_type == 'completo':
            # TODO -> GENERATE COMPLETE REPORT
            return False
