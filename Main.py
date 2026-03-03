from Conta import Conta
cc = Conta('1234', 'Juca', 1000)
print(f'Saldo: {cc.get_saldo()}')

cc.set_saldo(500)
print(f'Saldo: {cc.get_saldo()}')
cc.set_saldo(700)
