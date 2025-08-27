menor_valor = float('inf')
maior_valor = float('-inf')
print('Digite [0] para sair da repetição: ')

while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    if valor < menor_valor:
        menor = valor
    if valor > maior_valor:
        maior = valor



