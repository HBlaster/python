class Coordenada:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def distancia (self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__=='__main__':
    cord1 = Coordenada(3,30)
    cord2 = Coordenada(4,8)

    print('La distancia es:',cord1.distancia(cord2))