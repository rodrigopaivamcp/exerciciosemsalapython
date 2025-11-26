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
