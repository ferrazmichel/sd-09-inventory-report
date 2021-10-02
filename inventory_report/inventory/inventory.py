from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

from functools import lru_cache
from csv import DictReader
import json
from xml.etree import ElementTree
import os.path


class Inventory(CompleteReport, SimpleReport):

    """importa e cria uma lista do arquivo csv"""
    @lru_cache
    def import_data_csv(path):
        with open(path, 'r', encoding='utf8') as file:
            spam_reader = DictReader(file)
            read_list = [rows for rows in spam_reader]
            return read_list

    """importa e cria uma lista do arquivo json"""
    @lru_cache
    def import_data_json(path):
        with open(path) as file:
            json_reader = json.load(file)
            read_list = [rows for rows in json_reader]
            return read_list

    """importa e cria uma lista do arquivo xml"""
    @lru_cache
    def import_data_xml(path):
        tree = ElementTree.parse(path)
        root = tree.getroot()
        read_list = []
        for elem in root:
            items = {}
            for subelem in elem:
                items[subelem.tag] = subelem.text
            read_list.append(items)
        return read_list

    """escolhe o tipo da extenção do arquivo"""
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
