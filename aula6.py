class Veículo:
    def __init__(self, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def get_valor(self):
        return self.valor


    def set_modelo(self, novo):
        self.modelo = novo

    def set_ano(self, novo):
        self.ano = novo

    def set_valor(self, novo):
        self.valor = novo




if __name__ == '__main__':

    carro1 = Veículo('HB', 2024, 80000.00 )
    print("Endereço hexadecimal do objeto1:", carro1)


    carro2 = Veículo('Corolla', 2024, 190000.00 )
    print("Endereço hexadecimal do objeto2:", carro2)


    print('\nDados do carro1: \nModelo:', carro1.get_modelo())
    print('\nano:', carro1.get_ano())
    print('\nvalor:', carro1.get_valor())



    print('\nDados do carro1atualizado: \nModelo:', carro1.get_modelo())
    print('\nano:', carro1.get_ano())
    print('\nvalor:', carro1.get_valor())



    print('\n Dados do carro2: \nModelo:', carro2.get_modelo())
    print('\nano:', carro2.get_ano())
    print('\nvalor:', carro2.get_valor())

    carro1.set_modelo("Camaro")
    print(f"\nNome atualizado {carro1.get_modelo()}")

    carro1.set_ano("2015")
    print(f"\nano atualizado {carro1.get_ano()}")

    carro1.set_valor("1000000.00")
    print(f"\nvalor atualizado {carro1.get_valor()}")







