from datetime import date


class SimpleReport:
    @classmethod
    def generate(self, data):
        list = []
        container = []
        company = []
        for obj in data:
            list.append(obj["data_de_fabricacao"])
            if obj["data_de_validade"] > str(date.today()):
                container.append(obj["data_de_validade"])

        for obj in data:
            if obj["nome_da_empresa"] == obj["nome_da_empresa"]:
                company.append(obj["nome_da_empresa"])

        container.sort()

        response = (
            f"Data de fabricação mais antiga: {min(list)}\n"
            f"Data de validade mais próxima: {container[0]}\n"
            "Empresa com maior quantidade de produtos estocados: "
            f"{company[1]}\n"
        )

        return response
