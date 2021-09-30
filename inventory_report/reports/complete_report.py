from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class products_by_company:
    @classmethod
    def generate_report(cls, data_list):
        company_list = [item['nome_da_empresa'] for item in data_list]
        company_counter = Counter(company_list)
        company_report = ''
        for company in company_counter.keys():
            company_report += f'- {company}: {company_counter[company]}\n'
        return f'Produtos estocados por empresa: \n{company_report}'


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data_list):
        simple_report = super().generate(data_list)
        products_report = products_by_company.generate_report(data_list)
        return f'{simple_report}\n{products_report}'

