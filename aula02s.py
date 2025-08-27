ct = 0
soma = 0

print('Digite [-1] para sair da repetição')
nome = str(input('Digite o nome da disciplina: '))
while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota == -1:
        break
    ct = ct + 1
    soma = soma + nota
    media = soma/ct

print('Quantidade de notas digitadas: ', nota)
print('Soma das notas digitadas: ', soma)
print('Média das notas digitadas', media)
print('Nome da disciplina: ', nome)
