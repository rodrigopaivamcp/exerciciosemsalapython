import self
class Aluno:


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

    def set_nome(self, novo):
        self.nome = 'José'
    def set_mensalidade(self, novo):
        self.mensalidade = 1200.00
    def set_idade(self, novo):
        self.idade = 20


if __name__ == '__main__':
    joao = Aluno("João", 1100.00, 19)
    print('Endereço hexadecimal do João:', joao)

    joao.set_nome("José")
    print(f"Nome atualizado: {joao.get_nome()}")

    print("\n ")


    maria = Aluno("Maria", 1050.00, 17 )
    print('Endereço hexadecimal de Maria:', maria)

    print("\n- Aluno1")
    print("Nome:", joao.get_nome())
    print("Mensalidade:", joao.get_mensalidade())
    print("Idade:", joao.get_idade())

    print("\nNome atualizado")
    print("Nome:", joao.get_nome())
    print("Mensalidade:", joao.get_mensalidade())
    print("Idade:", joao.get_idade())

    print("\n- Aluno2")
    print("Nome:", maria.get_nome())
    print("Mensalidade:", maria.get_mensalidade())
    print("Idade:", maria.get_idade())












