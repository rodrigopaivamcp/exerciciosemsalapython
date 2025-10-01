from classes import Funcionario
from classes import Gerente


if __name__ == '__main__':
    funcionario1 = Funcionario(nome="Joao", salario= 3000)
    print(funcionario1)
    funcionario2 = Funcionario(nome="Maria", salario= 3050)
    print(funcionario2)

    print("Funcionário1:", funcionario1.get_nome(), "\nsalário:", funcionario1.get_salario())

    print("Funcionário2:", funcionario2.get_nome(), "\nsalário:", funcionario2.get_salario())


    gerente = Gerente(nome="Jorge", salario= 7000, qtd_gerencia= 2)
    print("Gerente:", gerente.get_nome(), "\nsalário:", gerente.get_salario(), "\nfuncionários sob gerência:", gerente.get_qtd_gerencia())

    funcionario1.set_nome("Carlos")
    funcionario1.set_salario(3500)
    funcionario1.set_bonificacao(1.1*3500)

    funcionario2.set_nome("Júlia")
    funcionario2.set_salario(3250)
    funcionario2.set_bonificacao(1.1*3250)


    gerente.set_nome("Alexandre")
    gerente.set_salario(8000)
    gerente.set_qtd_gerencia(3)
    gerente.set_bonificacao(1.2*8000)

    print("\nApós alterações usando setters")
    print("\nFuncionário1:", funcionario1.get_nome(), "\nsalário:", funcionario1.get_salario(), "\nsalário pós-bonificacao", funcionario1.get_bonificacao())
    print("\nFuncionário2:", funcionario2.get_nome(), "\nsalário:", funcionario2.get_salario(), "\nsalario pós-bonificacao", funcionario2.get_bonificacao())
    print("\nGerente:", gerente.get_nome(), "\nsalário:", gerente.get_salario(),"\nfuncionários sob gerência:", gerente.get_qtd_gerencia(),
          "\nsalario pós-bonificacao", gerente.get_bonificacao())
