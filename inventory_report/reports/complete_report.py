from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        simple_report = SimpleReport.generate(products)
        company_quantity = SimpleReport.get_stock_products(products)
        return f"{simple_report}\n{company_quantity}"
