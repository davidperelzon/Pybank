class Conta:
    def __init__(self, numero, titular, saldo):
        #_ protegido
        #__ privado
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
    #GET ==> captura a variavel
    def get_saldo(self):
        return self.__saldo

    #set altera a variavel
    def set_saldo(self, valor):
        if self.__saldo - valor < 0:
            print('Saldo insuficiente')
        else:
            self.__saldo -= valor
