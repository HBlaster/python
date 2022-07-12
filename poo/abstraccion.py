
class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenarDeAgua(temperatura)
        self._anadirJabon()
        self._lavar()
        self._centrifugar()

    def _llenarDeAgua(self, temperatura):
        print (f'llenando tanque con agua {temperatura}')
    
    def _anadirJabon(self):
        print('Anadiendo jabon')
    
    def _lavar(self):
        print('Lavar la ropa')

    def _centrifugar(self):
        print('Exprimir la ropa')


if __name__=='__main__':
    lavadora = Lavadora()
    lavadora.lavar()
