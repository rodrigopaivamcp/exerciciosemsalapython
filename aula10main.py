from aula10 import FormaGeometrica, Quadrado, Circulo

if __name__ == '__main__':
    qd1 = Quadrado(cor ='azul', lado= 2)
    print(qd1)

    print("\nQuadrado: ", qd1.get_cor(), "\nlado: ", qd1.get_cor(), "\narea:", qd1.get_area(), "\nperimetro", qd1.get_perimetro())

    qd1.set_cor('Verde')
    qd1.set_lado(9)

    crc = Circulo(cor='vermelho', raio=4)
    print('\n Circulo: ', crc.get_cor(), '\nRaio:', crc.get_raio(), crc.get_area(), crc.get_perimetro())

    crc.set_cor('Amarelo')
    crc.set_raio(5)

    print("\nApós alterações usando setters")
    print("\nQuadrado:", qd1.get_cor(), "\nLado:", qd1.get_lado())
    print("\nCirculo:", crc.get_cor(), "\nRaio:", crc.get_raio())
