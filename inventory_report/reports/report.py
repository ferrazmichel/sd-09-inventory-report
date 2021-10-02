from datetime import date


class Report():
    @classmethod
    def product_exp_imminent(cls, products):
        today_date = date.today().strftime('%Y-%m-%d')
        product_exp = min([
            product['data_de_validade']
            for product in products
            if product['data_de_validade'] >= today_date
        ])
        return f"Data de validade mais próxima: {product_exp}\n"

    @classmethod
    def get_company_with_more_products(cls, products):
        companies = [product['nome_da_empresa'] for product in products]
        stock = max(set(companies), key=companies.count)
        return f"Empresa com maior quantidade de produtos estocados: {stock}\n"

    @classmethod
    def get_last_manufacturing_date(cls, products):
        min_date = min([product['data_de_fabricacao'] for product in products])
        return f"Data de fabricação mais antiga: {min_date}\n"

    @classmethod
    def get_stock_products(cls, products):
        companies = []
        companies_set = set()
        for product in products:
            companies_set.add(product['nome_da_empresa'])
        company_quantity = 'Produtos estocados por empresa: \n'
        for company in companies_set:
            company_quantity += f"- {company}: {companies.count(company)}\n"
        return company_quantity

    @classmethod
    def generate(cls, products):
        raise NotImplementedError
