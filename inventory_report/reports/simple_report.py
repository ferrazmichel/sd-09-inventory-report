from datetime import datetime as dt
from collections import Counter


class create_report:
    @classmethod
    def oldest_manufacturing_date(cls, data_list):
        dates = [object["data_de_fabricacao"] for object in data_list]
        dates.sort()
        return dates[0]

    @classmethod
    def closest_valid_expiration_date(cls, data_list):
        current_date = dt.now().strftime("%Y-%m-%d")
        dates = [
            item["data_de_validade"]
            for item in data_list
            if item["data_de_validade"] > str(current_date)
        ]
        dates.sort()
        return dates[0]

    @classmethod
    def company_with_most_stock(cls, data_list):
        company_list = [item["nome_da_empresa"] for item in data_list]
        company_counter = Counter(company_list)
        return max(company_counter)


class SimpleReport:
    @classmethod
    def generate(self, data_list):
        oldest = create_report.oldest_manufacturing_date(data_list)
        expiring = create_report.closest_valid_expiration_date(data_list)
        top_company = create_report.company_with_most_stock(data_list)

        report_1 = f"Data de fabricação mais antiga: {oldest}"
        report_2 = f"Data de validade mais próxima: {expiring}"
        report_3_prefix = "Empresa com maior quantidade de produtos estocados:"
        report_3 = f'{report_3_prefix} {top_company}'

        return f"{report_1}\n{report_2}\n{report_3}\n"
