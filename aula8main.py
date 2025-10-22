from aula8classes import Veiculo
from aula8classes import Carro
from aula8classes import Moto

if __name__ == '__main__':
    veiculo1 = Veiculo(valor = 100000, km = 12000)
    print(veiculo1)

    veiculo2 = Veiculo(valor = 145000, km = 12550)
    print(veiculo2)

    print("\nVeiculo1:", veiculo1.get_valor(), "\nquilometragem:", veiculo1.get_km())

    print("\nVeiculo2:", veiculo2.get_valor(), "\nquilometragem:", veiculo2.get_km())

    veiculo1.set_valor(11400)
    veiculo1.set_km(12730)
    veiculo1.atualiza_valor(11900) # aumento de 500


    veiculo2.set_valor(14860)
    veiculo2.set_km(12890)
    veiculo2.atualiza_valor(14900) # aumento de 40

    carro = Carro(valor=140300, km=12590, modelo='Kwid')
    print("\nCarro:", carro.get_valor(), "\nkm:", carro.get_km(), "\nmodelo:", carro.get_modelo())

    carro.set_valor(149020)
    carro.set_km(11050)
    carro.set_modelo('kwid')

    moto = Moto(valor=148209, km=13212, modelo='CB-500', cilindrada = '500')
    print("\nMoto:", moto.get_valor(), "\nkm:", moto.get_km(), "\nmodelo:", moto.get_modelo(), "\ncilindrada:", moto.get_cilindrada())

    moto.set_valor(149100)
    moto.set_km(10789)
    moto.set_modelo('Vulcan')
    moto.set_cilindrada('700')


    print("\nApós alterações usando setters")
    print("\nVeiculo1:", veiculo1.get_valor(), "\nquilometragem:", veiculo1.get_km())
    print("\nVeiculo2:", veiculo2.get_valor(), "\nquilometragem:", veiculo2.get_km())
    print("\nCarro:", carro.get_valor(), "\nkm:", carro.get_km(), "\nmodelo:", carro.get_modelo())
    print("\nMoto:", moto.get_valor(), "\nkm:", moto.get_km(), "\nmodelo:", moto.get_modelo(), "\ncilindrada:", moto.get_cilindrada())



