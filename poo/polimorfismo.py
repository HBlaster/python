class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando en bicicleta')

def run():
    Persona1 = Persona(nombre = 'David')
    Persona1.avanza()

    Persona2 = Ciclista(nombre = 'Juan')
    Persona2.avanza()


if __name__=='__main__':
    run()
