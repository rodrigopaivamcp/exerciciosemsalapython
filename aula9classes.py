class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):
        return self.nome

    def get_saldo(self):
        return self.saldo

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_saldo(self, novo_saldo):
        self.saldo = novo_saldo

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def retirada(self, valor):
        self.saldo = self.saldo - valor



class PessoaFisica(Conta):
    def __init__(self, nome, saldo, genero):
        super().__init__(nome, saldo)
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_genero(self, novo_genero):
        self.genero = novo_genero

class PessoaJuridica(Conta):
    def __init__(self, nome, saldo, modalidade):
        super(). __init__(nome, saldo)
        self.modalidade = modalidade
    def get_modalidade(self):
        return self.modalidade
    def set_modalidade(self, nova_modalidade):
        self.modalidade = nova_modalidade



