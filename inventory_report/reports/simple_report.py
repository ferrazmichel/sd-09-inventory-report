from datetime import datetime as dt
from collections import Counter


class create_report:
    @classmethod
    def oldest_manufacturing_date(cls, object_list):
        dates = [object["data_de_fabricacao"] for object in object_list]
        dates.sort()
        return dates[0]

    @classmethod
    def closest_valid_expiration_date(cls, object_list):
        current_date = dt.now().strftime("%Y-%m-%d")
        dates = [
            object["data_de_validade"]
            for object in object_list
            if object["data_de_validade"] > str(current_date)
        ]
        dates.sort()
        return dates[0]

    @classmethod
    def company_with_most_stock(cls, object_list):
        company_list = [object["nome_da_empresa"] for object in object_list]
        company_counter = Counter(company_list)
        return max(company_counter)


class SimpleReport:
    @classmethod
    def generate(self, object_list):
        oldest = create_report.oldest_manufacturing_date(object_list)
        expiring = create_report.closest_valid_expiration_date(object_list)
        top_company = create_report.company_with_most_stock(object_list)

        report_1 = f"Data de fabricação mais antiga: {oldest}"
        report_2 = f"Data de validade mais próxima: {expiring}"
        report_3_prefix = "Empresa com maior quantidade de produtos estocados:"
        report_3 = f'{report_3_prefix} {top_company}'

        return f"{report_1}\n{report_2}\n{report_3}\n"
