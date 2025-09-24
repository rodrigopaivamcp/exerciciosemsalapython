ct_aluno = 0
soma_idade = 0
mais_novo= 200  # mais_novo = float('inf')
mais_velho = float('-inf')
ct_30 = 0
print('digite 0 para sair da repetição')

while True:
    idade = int(input('digite a idade do aluno: '))
    if idade == 0:
        break
    ct_aluno = ct_aluno + 1
    soma_idade = soma_idade + idade
    if idade < mais_novo:
        media = soma_idade/ct_aluno
        mais_novo = idade
    if idade > mais_velho:
        mais_velho = idade
    if idade > 30:
        ct_30 = ct_30 + 1   # ct_30 += 1



print(f'a media de idade da turma é de {media} anos')
print(f'o aluno mais novo tem {mais_novo}')
print(f'a quantidade de alunos é {ct_aluno}')
print(f'a soma das idades dos alunos é {soma_idade}')
print(f'a idade do aluno mais velho é {mais_velho} anos')
print(f'a quantidade de alunos com mais de 30 anos é de {ct_30}')
