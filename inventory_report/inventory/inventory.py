from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import csv
import xmltodict


class Inventory:
    # Método para verificar os ultimos caracteres de uma string
    # https://www.w3schools.com/python/ref_string_endswith.asp
    @classmethod
    def get_data_by_file_type(cls, file_path):
        # Para casos em que tenhamos a extensão com letras maiusculas
        file_path = file_path.lower()
        with open(file_path, 'r') as raw_data:
            if file_path.endswith('.json'):
                return json.load(raw_data)
            elif file_path.endswith('.csv'):
                # Tem que transformar em uma lista
                return list(csv.DictReader(raw_data))
            elif file_path.endswith('.xml'):
                # https://linuxhint.com/python_xml_to_dictionary/
                # https://omz-software.com/pythonista/docs/ios/xmltodict.html
                # https://stackoverflow.com/questions/40154727/how-to-use-xmltodict-to-get-items-out-of-an-xml-file
                data = xmltodict.parse(raw_data.read())
                data = [dict(entry) for entry in data['dataset']['record']]
                return data

    @classmethod
    def import_data(cls, file_path, report_type):
        file_content = cls.get_data_by_file_type(file_path)
        if report_type == "simples":
            return SimpleReport.generate(file_content)
        elif report_type == "completo":
            return CompleteReport.generate(file_content)

