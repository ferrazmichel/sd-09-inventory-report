from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def get_enterprises_list(products):
        enterprises_list = [product["nome_da_empresa"] for product in products]
        return Counter(enterprises_list)

    @classmethod
    def generate(cls, dictList):
        simple_report = SimpleReport.generate(dictList)
        enterprises_list = cls.get_enterprises_list(dictList)

        message = "Produtos estocados por empresa: \n"
        for enterprise in enterprises_list:
            message += f"- {enterprise}: {enterprises_list[enterprise]}\n"
        return (
          f"{simple_report}\n{message}"
        )
