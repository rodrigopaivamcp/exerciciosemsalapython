from aula9classes import Conta
from aula9classes import PessoaFisica
from aula9classes import PessoaJuridica

if __name__ =='__main__':
    conta1 = Conta(nome= 'Joao', saldo = 8000)
    print(conta1)

    conta2 = Conta(nome= 'Maria', saldo = 9050)
    print(conta2)

    print("\n Conta1: ", conta1.get_nome(), "\nSaldo:", conta1.get_saldo())
    print("\n Conta2: ", conta2.get_nome(), "\nSaldo:", conta2.get_saldo())

    conta1.set_nome('Gabriel')
    conta1.set_saldo(5750)

    conta2.set_nome('Julia')
    conta2.set_saldo(8040)

    fisica1 = PessoaFisica(nome = 'Joao', saldo = 8000, genero = 'masculino')
    print('\n PessoaFisica1: ', fisica1.get_nome(), '\nSaldo:', fisica1.get_saldo(), '\nGenero: ', fisica1.get_genero())

    fisica1.set_nome('Gabriel')
    fisica1.set_saldo(8900)
    fisica1.set_genero('masculino')

    fisica2 = PessoaFisica(nome = 'Maria', saldo = 9050, genero = 'feminino')
    print('\n PessoaFisica2: ', fisica2.get_nome(), '\nSaldo:', fisica2.get_saldo(), '\nGenero: ', fisica2.get_genero())

    fisica2.set_nome('Julia')
    fisica2.set_saldo(9060)
    fisica2.set_genero('feminino')


    juridica1 = PessoaJuridica(nome = 'Joao', saldo = 8000, modalidade = 'MEI')
    print('\n PessoaJuridica1: ', juridica1.get_nome(), '\nSaldo:', juridica1.get_saldo(), '\nModalidade: ', juridica1.get_modalidade())

    juridica1.set_nome('Gabriel')
    juridica1.set_saldo(8900)
    juridica1.set_modalidade('ME')

    juridica2 = PessoaJuridica(nome = 'Maria', saldo = 9050, modalidade = 'LTDA')
    print('\n PessoaJuridica2: ', juridica2.get_nome(), '\nSaldo:', juridica2.get_saldo(), '\nModalidade: ', juridica2.get_modalidade())

    juridica2.set_nome('Julia')
    juridica2.set_saldo(9060)
    juridica2.set_modalidade('SA')


    print("\nApós alterações usando setters")
    print("\nConta1:", conta1.get_nome(), "\nSaldo:", conta1.get_saldo())
    print("\nConta2:", conta2.get_nome(), "\nSaldo:", conta2.get_saldo())
    print("\nPessoaFisica1:", fisica1.get_nome(), "\nSaldo:", fisica1.get_saldo(), "\nGenero:", fisica1.get_genero())
    print("\nPessoaFisica1:", fisica1.get_nome(), "\nSaldo:", fisica1.get_saldo(), "\nGenero:", fisica1.get_genero())
    print("\nPessoaJuridica1:", juridica1.get_nome(), "\nsaldo:", juridica1.get_saldo(), "\nmodalidade:", juridica1.get_modalidade())
    print("\nPessoaJuridica2:", juridica2.get_nome(), "\nsaldo:", juridica2.get_saldo(), "\nmodalidade:", juridica2.get_modalidade())

    juridica2.deposito(2300)
    print("\nApós depósito em PessoaJuridica2:")
    print("Saldo atualizado:", juridica2.get_saldo())







