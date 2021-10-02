from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def get_company_names_and_quantity(obj_list):
        company_names = [company["nome_da_empresa"] for company in obj_list]
        names_quantity = "Produtos estocados por empresa: \n"
        for name in company_names:
            if name not in names_quantity:
                names_quantity += f"- {name}: {company_names.count(name)}\n"
        return names_quantity

    @classmethod
    def generate(cls, obj_list=[{}]):
        simple_report = SimpleReport.generate(obj_list)
        names_quantity = cls.get_company_names_and_quantity(obj_list)

        return f"{simple_report}\n{names_quantity}"
