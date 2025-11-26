class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, nome, saldo, cheque=0):
        super().__init__(nome, saldo)
        self.cheque = cheque

    def get_cheque(self):
        return self.cheque

    def set_cheque(self, novo_cheque):
        self.cheque = novo_cheque


    def saldo_total(self):
        saldo_total = self.saldo + self.cheque
        return saldo_total

class ContaPoupanca(Conta):
    def __init__(self, nome, saldo, rendimento=1.5):
        super().__init__(nome, saldo)
        self.rendimento = rendimento

    def get_rendimento(self):
        return self.rendimento

    def set_rendimento(self, novo_rendimento):
        self.rendimento = novo_rendimento

    def saldo_atualizado(self):
        saldo_atualizado = self.saldo + self.rendimento
        return saldo_atualizado



