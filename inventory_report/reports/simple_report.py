from datetime import datetime


class filter_info:
    @staticmethod
    def oldest_manufacture(list):
        oldest_date = min([item["data_de_fabricacao"] for item in list])
        return oldest_date

    @staticmethod
    def next_exipred_date(list):
        current_date = datetime.now().strftime("%Y-%m-%d")
        dates = [
            row["data_de_validade"]
            for row in list
            if row["data_de_validade"] >= current_date
        ]
        dates.sort()
        return dates[0]

    # lógica retirada de:
    # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    @staticmethod
    def best_company(list):
        companies = [row["nome_da_empresa"] for row in list]
        return max(set(companies), key=companies.count)


class SimpleReport:
    @staticmethod
    def generate(list):
        man_date = filter_info.oldest_manufacture(list)
        exp_date = filter_info.next_exipred_date(list)
        best_cmp = filter_info.best_company(list)
        return (
            f"Data de fabricação mais antiga: {man_date}\n"
            f"Data de validade mais próxima: {exp_date}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {best_cmp}\n"
        )
