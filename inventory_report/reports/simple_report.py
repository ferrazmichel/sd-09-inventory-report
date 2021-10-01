from datetime import datetime
from collections import Counter


class SimpleReport:

    def get_oldest_fabricated_date(obj_list):
        return min(
            item["data_de_fabricacao"] for item in obj_list
        )

    def get_closest_expiration_date(obj_list):
        today = datetime.today().strftime("%Y-%m-%d")
        return min(
            item["data_de_validade"]
            for item in obj_list
            if item["data_de_validade"] > today
        )

    def get_company_name_with_greater_stock(obj_list):
        return Counter(
            item["nome_da_empresa"] for item in obj_list
        ).most_common()[0][0]

    @classmethod
    def generate(cls, obj_list=[{}]):
        return (
            f"Data de fabricação mais antiga: "
            f"{cls.get_oldest_fabricated_date(obj_list)}\n"
            f"Data de validade mais próxima: "
            f"{cls.get_closest_expiration_date(obj_list)}\n"
            f"Empresa com maior quantidade de produtos estocados: "
            f"{cls.get_company_name_with_greater_stock(obj_list)}\n"
        )
