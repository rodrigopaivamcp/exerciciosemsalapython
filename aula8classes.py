class Veiculo:
    def __init__(self, valor, km):
        self.valor = valor
        self.km = km

    def get_valor(self):
        return self.valor

    def get_km(self):
        return self.km

    def set_valor(self, novo_valor):
        self.valor = novo_valor

    def set_km(self, nova_km):
        self.km = nova_km

    def atualiza_valor(self, valor_atualizado):
        self.valor_atualizado = valor + (aumento * valor)


class Carro(Veiculo):
    def __init__(self, valor, km, modelo, atualiza_valor):
        super().__init__(valor, km)
        self.modelo = modelo

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, novo_modelo):
        self.modelo = novo_modelo

class Moto(Veiculo):
    def __init__(self, valor, km, modelo, cilindrada, atualiza_valor):
        super().__init__(valor, km)
        self.modelo = modelo
        self.cilindrada = cilindrada

    def get_modelo(self):
        return self.modelo

    def get_cilindrada(self):
        return self.cilindrada

    def set_modelo(self, novo_modelo):
         self.modelo = novo_modelo

    def set_cilindrada(self, novo_cilindrada):
         self.cilindrada = novo_cilindrada


