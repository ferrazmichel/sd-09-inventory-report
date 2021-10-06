# Entrada
# [
#   {
#     "id": 1,
#     "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
#     "nome_da_empresa": "Forces of Nature",
#     "data_de_fabricacao": "2020-07-04",
#     "data_de_validade": "2023-02-09",
#     "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
#     "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
#   }
# ]

# Saida
# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA


from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(cls, products):
        oldest_fabrication = min(
            product["data_de_fabricacao"] for product in products
        )

        now = datetime.now()
        next_expiration = min(
          product["data_de_validade"] for product in products
          if now < datetime.strptime(product["data_de_validade"], "%Y-%m-%d")
        )

        more_stock = max(Counter(product["nome_da_empresa"]
                         for product in products))

        return (
          f'''
          Data de fabricação mais antiga: {oldest_fabrication}
          Data de validade mais próxima: {next_expiration}
          Empresa com maior quantidade de produtos estocados: {more_stock}'''
        )

# Uso do Datetime e a conversão da string para fins de calculo
# https://www.programiz.com/python-programming/datetime/current-datetime
# https://www.educative.io/edpresso/how-to-convert-a-string-to-a-date-in-python