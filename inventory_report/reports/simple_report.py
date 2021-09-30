from datetime import datetime
# https://www.guru99.com/python-counter-collections-example.html
# Counter utilizado para contar quantas vezes cada empresa aparece na lista
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, product_list):
        dates = [product["data_de_fabricacao"] for product in product_list]
        dates.sort()
        earliest_manufacture_date = dates[0]

        current_date = datetime.now().strftime("%Y-%m-%d")
        closest_expiration_date = [
            product["data_de_validade"] for product in product_list
            if product["data_de_validade"] > current_date
        ]
        closest_expiration_date.sort()

        companies = [product["nome_da_empresa"] for product in product_list]
        company_greatest_stocked_products = (
          max(Counter(companies))
        )

        prefix = "Empresa com maior quantidade de produtos estocados:"

        return (
          f"Data de fabricação mais antiga: {earliest_manufacture_date}\n"
          f"Data de validade mais próxima: {closest_expiration_date[0]}\n"
          f"{prefix} {company_greatest_stocked_products}\n"
          )
