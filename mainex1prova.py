from ex1prova import Conta, ContaCorrente

if __name__ == '__main__':
    c1 = Conta('João', 1500)
    print(c1)

    print('Conta\n Saldo:', c1.get_saldo())

    cc1 = ContaCorrente(nome = 'Maria', saldo = 1200, cheque = 100)
    print(cc1)

    print('Saldo:', cc1.get_saldo())
    print('Cheque:', cc1.get_cheque)
    cc1.set_cheque(200)
    print('Cheque atualizado:', cc1.get_cheque())
    print('Saldo total:', cc1.saldo_total())
