from datetime import datetime
from collections import Counter


class SimpleReport:
    def generate(obj_list=[{}]):
        today = datetime.today().strftime("%Y-%m-%d")
        oldest_fabricated_date = min(
            item["data_de_fabricacao"] for item in obj_list
        )
        closest_expiration_date = min(
            item["data_de_validade"]
            for item in obj_list
            if item["data_de_validade"] > today
        )

        name = Counter(
            item["nome_da_empresa"] for item in obj_list
        ).most_common()[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_fabricated_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com maior quantidade de produtos estocados: {name}\n"
        )
