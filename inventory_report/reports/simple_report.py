from datetime import date


class SimpleReport:
    def generate(data):  # posso receber um "JSON" e fazer um "parse" p/ string
        today = date.today()
        manufacturing_date = []
        expiration_date = []
        inventory = []

        for product in data:
            manufacturing_date.append(product["data_de_fabricação"])
            if product["data_de_validade"] > today.strftime("%Y-%m-%d"):
                expiration_date.append(product["data_de_validade"])
            inventory.append(product["nome_da_empresa"])

        big_stock = max(inventory)

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date)}\n"
            f"Data de validade mais próxima: {min(expiration_date)}\n"
            f"Empresa com maior quantidade de produtos estocados: {big_stock}"
        )
