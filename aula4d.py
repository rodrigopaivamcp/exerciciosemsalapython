def maximo (num1, num2):
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    return maior

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
vl_retorno = maximo(numero1, numero2)
print("\nMaior valor:", vl_retorno)