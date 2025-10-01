class funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario

class gerente:
    def __init__(self, nome, salario, funcionario):
        self.nome = nome
        self.salario = salario
        self.funcionario = funcionario

    def get_nome(self):
        return self.nome
    def get_salario(self):
        return self.salario
    def get_funcionario(self):
        return self.funcionario
