from classes import funcionario
from classes import gerente


if __name__ == '__main__':
    funcionario1 = funcionario(nome="Joao", salario= 3000)
    print(funcionario1)
    funcionario2 = funcionario(nome="Maria", salario= 3050)
    print(funcionario2)

    print("Funcionário1:", funcionario1.get_nome(), "\nsalário:", funcionario1.get_salario())

    print("Funcionário2:", funcionario2.get_nome(), "\nsalário:", funcionario2.get_salario())


    gerente = gerente(nome="Jorge", salario= 7000, funcionario= 2)
    print("Gerente:", gerente.get_nome(), "\nsalário:", gerente.get_salario(), "\nfuncionários sob gerência:", gerente.get_funcionario())