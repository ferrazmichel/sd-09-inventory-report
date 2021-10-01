import datetime
from typing import Counter


class Manage_list:
    """converte a data de string pra date"""
    @staticmethod
    def convert_data(date_string):
        format_string = '%Y-%m-%d'
        date_corretc = datetime.datetime.strptime(
            date_string, format_string
        ).date()
        return date_corretc

    """faz o calculo dos dias"""
    @staticmethod
    def subtract_days(date_value):
        date_now = datetime.date.today()
        date_end = Manage_list.convert_data(date_value)
        result = abs((date_end - date_now).days)
        return result

    """seleciona o mais velho fabricado"""
    @staticmethod
    def old_item(list):
        data_sorted = sorted(list, key=lambda k: k['data_de_fabricacao'])
        return data_sorted[0].get('data_de_fabricacao')

    """seleciona o mais perto de vencer a validade"""
    @staticmethod
    def validate_closest(list):
        min_days = []
        for item in list:
            days = Manage_list.subtract_days(item.get('data_de_validade'))
            min_days.append(days)
        min_value = min(min_days)
        return list[min_days.index(min_value)].get('data_de_validade')

    """conta qual empresa tem o maior volume de estoque com opçao 0
    e todos estoques opçao n"""
    @staticmethod
    def count_stock(list, option):
        list_names = [name['nome_da_empresa'] for name in list]
        ocorrencias = Counter(list_names)
        if (option == 0):
            return max(set(list_names), key=list_names.count)
        else:
            return ocorrencias


class SimpleReport:
    """gerador de relatorio"""
    @staticmethod
    def generate(list):
        result_old = Manage_list.old_item(list)
        result_closest = Manage_list.validate_closest(list)
        result_stock = Manage_list.count_stock(list, 0)

        return (
            'Data de fabricação mais antiga: {}\n'
            'Data de validade mais próxima: {}\n'
            'Empresa com maior quantidade de produtos estocados: {}\n'
            .format(result_old, result_closest, result_stock)
        )
