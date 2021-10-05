from .simple_report import SimpleReport

from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, dict_list):

        inherited_method = super().generate(dict_list)
        company = []
        for row in dict_list:
            company.append(row["nome_da_empresa"])

        company_counter = Counter(company)

        container = []

        for row in company_counter:
            container.append(f"- {row}: {company_counter[row]}\n")

        response = "".join(map(str, container))

        result = (
            f"{inherited_method}\n"
            "Produtos estocados por empresa: \n"
            f"{response}"
        )

        return result
