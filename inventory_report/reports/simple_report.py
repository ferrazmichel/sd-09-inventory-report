from datetime import datetime
from collections import Counter


class SimpleReport:
    def get_oldest_fabrication_date(products):
        return min([product["data_de_fabricacao"] for product in products])

    def get_actual_expiration_date(products):
        actual_date = datetime.now().strftime("%Y-%m-%d")
        return min(
            [
                product["data_de_validade"]
                for product in products
                if actual_date < product["data_de_validade"]
            ]
        )

    def get_enterprise_bigger_stock(products):
        enterprises_names = [
            products["nome_da_empresa"] for products in products
        ]
        return max(Counter(enterprises_names))

    @classmethod
    def generate(cls, dictList):
        oldest_fabrication_date = cls.get_oldest_fabrication_date(dictList)
        actual_expiration_date = cls.get_actual_expiration_date(dictList)
        bigger_stock_enterprise = cls.get_enterprise_bigger_stock(dictList)
        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {actual_expiration_date}\n"
            f"Empresa com maior quantidade de produtos "
            f"estocados: {bigger_stock_enterprise}\n"
        )
