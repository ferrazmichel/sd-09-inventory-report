from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class company_report:
    @classmethod
    def products_quantity(cls, list):
        companies_list = [
            row["nome_da_empresa"]
            for row in list
        ]
        companies_quantity = Counter(companies_list)
        companies_product_report = ""
        for row in companies_quantity:
            companies_product_report += f"- {row}: {companies_quantity[row]}\n"
        return f"Produtos estocados por empresa: \n{companies_product_report}"


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, list):
        simple_rep = SimpleReport.generate(list)
        complete_rep = company_report.products_quantity(list)
        return f"{simple_rep}\n{complete_rep}"
