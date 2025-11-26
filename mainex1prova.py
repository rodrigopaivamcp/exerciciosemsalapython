from ex1prova import Conta, ContaCorrente, ContaPoupanca

if __name__ == '__main__':
    c1 = Conta('João', 1500)
    print('Conta')

    print('Conta\nSaldo:', c1.get_saldo())

    cc1 = ContaCorrente(nome = 'Maria', saldo = 1200, cheque = 100)
    print('---Conta Corrente---')

    print('Saldo:', cc1.get_saldo())
    print('Cheque:', cc1.get_cheque())
    cc1.set_cheque(200)
    print('Cheque atualizado:', cc1.get_cheque())
    print('Saldo total:', cc1.saldo_total())

    cp1 = ContaPoupanca('Gabriel', 5100, 2)
    print('---Conta Poupanca---')

    print('Saldo:', cp1.get_saldo())
    print('Rendimento:', cp1.get_rendimento())
    cp1.set_rendimento(2.5)
    print('Novo_rendimento:', cp1.get_rendimento())
    print('Saldo atualizado:', cp1.saldo_atualizado())

