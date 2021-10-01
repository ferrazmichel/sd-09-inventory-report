from inventory_report.reports.simple_report import SimpleReport, Manage_list


class CompleteReport(SimpleReport, Manage_list):
    """gerador de relatorio - herdada da classe SimpleReport"""
    @staticmethod
    def generate(list):
        result_simple_report = SimpleReport.generate(list)
        result_manage_list = Manage_list.count_stock(list, 1)

        """monta a segunda parte da string para retorno"""
        companies_rows = ''
        for key, value in result_manage_list.items():
            companies_rows += '- {}: {}\n'.format(key, value)

        return (
            '{}\n'
            'Produtos estocados por empresa: \n'
            '{}'
            .format(result_simple_report, companies_rows)
        )
