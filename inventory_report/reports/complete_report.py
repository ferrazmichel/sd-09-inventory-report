from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, dictList):
        simple_report = super().generate(dictList)
        quantidade_empresa = {}
        for list in dictList:
            empresa = list["nome_da_empresa"]
            contador = 0
            for list2 in dictList:
                if list2["nome_da_empresa"] == empresa:
                    contador += 1

            quantidade_empresa[empresa] = contador
        mensagem_de_quantidade = ""
        for item in quantidade_empresa:
            mensagem_de_quantidade += f"- {item}: {quantidade_empresa[item]}\n"

        return (
            f"{simple_report}\n" +
            "Produtos estocados por empresa: \n"
            f"{mensagem_de_quantidade}"
        )
