ct = 0
soma = 0

print('Digite [-1] para sair da repetição')
while True:
    numero = int(input('Digite um número: '))
    if numero == -1:
        break
    ct = ct + 1
    soma = soma + numero



print('Quantidade de números digitados: ', ct)
print('Soma dos valores digitados: ', soma)
