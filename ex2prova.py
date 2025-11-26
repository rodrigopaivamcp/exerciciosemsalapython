from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    @abstractmethod
    def calcular_preco(self):
        pass

    @abstractmethod
    def calcular_desconto(self):
        pass

class ProdutoFisico(Produto):
    def __init__(self, nome, preco_base, peso=1):
        super().__init__(nome, preco_base)
        self.peso = peso

    def calcular_preco(self):
        preco_total = self.preco_base + (self.peso * 4)
        return preco_total

    def calcular_desconto(self):
        vl_desconto = self.preco_base * 0.05
        return vl_desconto

class ProdutoDigital(Produto):
    def __init__(self, nome, preco_base, tamanho_mb=4):
        super().__init__(nome, preco_base)
        self.tamanho_mb = tamanho_mb

    def calcula_preco(self):
        preco_total = self.preco_base + 1 * self.tamanho_mb
        return preco_total

    def calcula_desconto(self):
        vl_desconto = self.preco_base * 0.11


