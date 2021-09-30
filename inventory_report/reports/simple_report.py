from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(list):
        closestValidy = SimpleReport.get_closest_validy(list)
        olderFabrication = SimpleReport.get_older_fabrication(list)
        mostStocked = SimpleReport.get_company_with_more_stocked(list)

        return (
            f"Data de fabricação mais antiga: {olderFabrication}\n"
            f"Data de validade mais próxima: {closestValidy}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {mostStocked}\n"
        )

    @staticmethod
    def get_closest_validy(list):
        current_date = datetime.now().strftime("%Y-%m-%d")
        dates = [
            product["data_de_validade"]
            for product in list
            if product["data_de_validade"] >= current_date
        ]
        dates.sort()
        return dates[0]

    @staticmethod
    def get_older_fabrication(list):
        fabrication_dates = [product["data_de_fabricacao"] for product in list]
        fabrication_dates.sort()
        return fabrication_dates[0]

    # Referência:
    # https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/

    @staticmethod
    def get_company_with_more_stocked(list):
        companies = [product["nome_da_empresa"] for product in list]
        return max(set(companies), key=companies.count)
