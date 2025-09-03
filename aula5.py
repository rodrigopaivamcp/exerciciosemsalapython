# import self
class NomeClasse:


    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
            return self.nome
    def get_mensalidade(self):
            return self.mensalidade
    def get_idade(self):
            return self.idade

if __name__ == '__main__':
    joao = NomeClasse("João", 1100.00, 19)
    print('Endereço hexadecimal do João:', joao)

    maria = NomeClasse("Maria", 1050.00, 17 )
    print('Endereço hexadecimal de Maria:', maria)

    print("\n- Aluno1")
    print("Nome:", joao.get_nome())
    print("Mensalidade:", joao.get_mensalidade())
    print("Idade:", joao.get_idade())

    print("\n- Aluno2")
    print("Nome:", maria.get_nome())
    print("Mensalidade:", maria.get_mensalidade())
    print("Idade:", maria.get_idade())









    print("- Aluno2\nNome:", maria.get_nome())








