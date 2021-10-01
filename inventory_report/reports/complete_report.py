from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(data):
        quantity_items = []
        for quantity in data:
            company_name = quantity["nome_da_empresa"]
            quantity_items.append(f"{company_name}")
        quantity_in_stock = dict(Counter(quantity_items))

        text = ''
        for key, value in quantity_in_stock.items():
            text += f'- {key}: {value}\n'

        return (
            f"{SimpleReport.generate(data)}\n"
            "Produtos estocados por empresa: \n"
            f"{text}"
        )
