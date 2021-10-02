from inventory_report.reports.report import Report


class SimpleReport(Report):
    # Para que seja possível usar a função generate sem instanciar SimpleReport
    @classmethod
    def generate(cls, products):
        return (
            f"{Report.get_last_manufacturing_date(products)}"
            f"{Report.product_exp_imminent(products)}"
            f"{Report.get_company_with_more_products(products)}"
        )
