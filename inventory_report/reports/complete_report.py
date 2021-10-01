from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(obj_list=[{}]):

        return (
            f"{SimpleReport(obj_list)}\nProdutos estocados por empresa:"
        )


lista = [
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
            "nome_da_empresa": "Newton Laboratories, Inc.",
            "data_de_fabricacao": "2019-11-08",
            "data_de_validade": "2019-11-25",
            "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
            "instrucoes_de_armazenamento": "velit eu est congue elementum",
        },
    ]

# CompleteReport(lista)




'''
2 - Criar um método generate numa classe CompleteReport do módulo inventory_report/reports/complete_report.py. Esse método deverá receber dados numa lista contendo estruturas do tipo dict e deverá retornar uma string formatada como um relatório.
A classe CompleteReport deve herdar o método (generate) da classe SimpleReport, de modo a especializar seu comportamento.

O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

[
  {
    "id": 1,
    "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP, GERANIUM MACULATUM ROOT, SODIUM CHLORIDE, THUJA OCCIDENTALIS LEAFY TWIG, ZINC, and ECHINACEA ANGUSTIFOLIA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
    "instrucoes_de_armazenamento": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque ultrices    phasellus"
  }
]
O método deverá retornar uma saída com o seguinte formato:

Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com maior quantidade de produtos estocados: NOME DA EMPRESA

Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
As seguintes verificações serão feitas:
2.1 - Será validado que é possível que o método generate da classe CompleteReport retorne a data de fabricação mais antiga

2.2 - Será validado que é possível que o método generate da classe CompleteReport retorne a validade de fabricação mais próxima

2.3 - Será validado que é possível que o método generate da classe CompleteReport retorne a empresa com maior estoque

2.4 - Será validado que é possível que o método generate da classe CompleteReport retorne a quantidade de produtos por empresa

2.5 - Será validado que é possível que o método generate da classe CompleteReport retorne o relatório no formato correto
'''