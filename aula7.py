ct_aluno = 0
soma_idade = 0
mais_novo= 200
print('digite 0 para sair da repetição')

while True:
    idade = float(input('digite a idade do aluno: '))
    if idade == 0:
        break
    ct_aluno = ct_aluno + 1
    soma_idade = soma_idade + idade
    if idade < mais_novo:
        media = soma_idade/ct_aluno

print(f'a media de idade da turma é de {media} anos')
