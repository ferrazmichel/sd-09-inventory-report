from datetime import date


class SimpleReport:
    # Para que seja possível usar a função generate sem instanciar SimpleReport
    @classmethod
    def generate(cls, products):
        today_date = date.today().strftime('%Y-%m-%d')

        products_exp_date = [
            product['data_de_validade']
            for product in products
            if product['data_de_validade'] >= today_date
        ]

        min_date = min([product['data_de_fabricacao'] for product in products])
        exp_imminent = min(products_exp_date)

        companies = [product['nome_da_empresa'] for product in products]
        stock = max(set(companies), key=companies.count)

        return (
            f"Data de fabricação mais antiga: {min_date}\n"
            f"Data de validade mais próxima: {exp_imminent}\n"
            f"Empresa com maior quantidade de produtos estocados: {stock}\n"
        )
