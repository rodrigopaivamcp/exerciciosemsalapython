def maximo (X,Y):
    if X > Y:
        maior = X
    else:
        maior = Y
    return maior
X = int(input('Primeiro valor:'))
Y = int(input('Segundo valor: '))

print('Maior valor: ', maximo(X,Y))
