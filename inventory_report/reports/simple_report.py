from datetime import datetime


class SimpleReport:
    def maior_estoque(estoque_empresa):
        num_empresa_mais_comum = 0
        empresa_com_mais_produtos = ""
        for empresa in estoque_empresa:
            if estoque_empresa.count(empresa) > num_empresa_mais_comum:
                num_empresa_mais_comum = estoque_empresa.count(empresa)
                empresa_com_mais_produtos = empresa

        return empresa_com_mais_produtos

    def generate(dictList):
        data_fabricacao_mais_antiga = "9999-99-99"
        data_validade_mais_proxima = "9999-99-99"
        estoque_empresa = []
        for line in dictList:
            # estoque = len(line["nome_do_produto"].split(","))
            if (line["data_de_fabricacao"] < data_fabricacao_mais_antiga):
                data_fabricacao_mais_antiga = line["data_de_fabricacao"]
            if (line["data_de_validade"] < data_validade_mais_proxima):
                str_date = line["data_de_validade"]
                data = datetime.strptime(str_date, "%Y-%m-%d")
                if (data > datetime.now()):
                    data_validade_mais_proxima = line["data_de_validade"]

            empresa = line["nome_da_empresa"]
            estoque_empresa.append(empresa)

        empresa_com_mais_produtos = SimpleReport.maior_estoque(estoque_empresa)

        return (
            "Data de fabricação mais antiga: " +
            f"{data_fabricacao_mais_antiga}\n" +
            f"Data de validade mais próxima: {data_validade_mais_proxima}\n" +
            "Empresa com maior quantidade de produtos " +
            f"estocados: {empresa_com_mais_produtos}\n"
            )
