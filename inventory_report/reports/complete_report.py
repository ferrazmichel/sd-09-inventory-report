from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, product_list):
        report_simple = super().generate(product_list)
        companies = [product["nome_da_empresa"] for product in product_list]
        companies_counter = Counter(companies)
        report_supplement = ""
        for company, quantity in companies_counter.items():
            report_supplement += f"- {company}: {quantity}\n"
        return (
          f"{report_simple}\n"
          f"Produtos estocados por empresa: \n"
          f"{report_supplement}"
          )
