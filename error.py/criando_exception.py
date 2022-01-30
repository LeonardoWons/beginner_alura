


class OperacaoFinanceiraError(Exception):
    pass


class SaldoInsuficienteError(Exception):

    def __init__(self, message="", saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = "saldo insuficiente\n" f"Saldo atual:{self.saldo} Valor a movimentar:{self.valor}"
        self.msg = message or msg
        super(SaldoInsuficienteError, self).__init__(self.msg, self.saldo, self.valor, *args)
