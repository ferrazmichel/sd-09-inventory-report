from inventory_report.reports.simple_report import SimpleReport

# ---inicio Teste local
# try:
#     import sys
#     import os

#     sys.path.append(
#         os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
#     )
# except ImportError:
#     raise


# from simple_report import SimpleReport
# ---Fim Teste Local

class CompleteReport(SimpleReport):
    @staticmethod
    def estoque_empresa(nome_da_empresa, dados):
        # print(nome_da_empresa)
        # print(dados)
        estoque = len(
            list(
                filter(
                    lambda el: el["nome_da_empresa"] == nome_da_empresa, dados
                )
            )
        )
        # print(estoque)
        return estoque

    @classmethod
    def generate(cls, dados):
        # print(dados)
        result_simple_report = super().generate(dados)
        # nome_empresa = "sanofi-aventis U.S. LLC"
        # cls.estoque_empresa(nome_empresa, dados)
        map_empresas = list(set(map(lambda el: el["nome_da_empresa"], dados)))
        map_result = list(
            (
                map(
                    lambda el: f"- {el}: {cls.estoque_empresa(el, dados)}\n",
                    map_empresas,
                )
            )
        )
        # print(map_empresas)
        # print(map_result)

        return (
            f"{result_simple_report}"
            f"Produtos estocados por empresa: \n"
            f"{''.join(map_result)}"
        )


# RETORNOS:

# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA
# Produtos estocados por empresa:
# - Physicians Total Care, Inc.: QUANTIDADE
# - Newton Laboratories, Inc.: QUANTIDADE
# - Forces of Nature: QUANTIDADE

# Teste local:
def stock():
    return [
        {
            "id": 1,
            "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2020-07-04",
            "data_de_validade": "2023-02-09",
            "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
            "instrucoes_de_armazenamento": "in blandit ultrices enim",
        },
        {
            "id": 2,
            "nome_do_produto": "sodium ferric gluconate complex",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2020-05-31",
            "data_de_validade": "2023-01-17",
            "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
            "instrucoes_de_armazenamento": "duis bibendum morbi",
        },
        {
            "id": 3,
            "nome_do_produto": "Dexamethasone Sodium Phosphate",
            "nome_da_empresa": "sanofi-aventis U.S. LLC",
            "data_de_fabricacao": "2019-09-13",
            "data_de_validade": "2023-02-13",
            "numero_de_serie": "BA52 2034 8595 7904 7131",
            "instrucoes_de_armazenamento": "morbi quis tortor id",
        },
        {
            "id": 4,
            "nome_do_produto": "Uricum acidum, Benzoicum acidum",
            "nome_da_empresa": "Newton Laboratories",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]


dados_teste = stock()
# print(dados_teste)
teste = CompleteReport.generate(dados_teste)
print(teste)
