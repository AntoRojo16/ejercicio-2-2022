from ManejadorDeViajeros import ListaViajeros

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            0:self.salir
                          }
    def opcion(self,op,lista,i):
        print(op)
        func=self.__switcher.get(op,lambda: print("Opción no válida"))
        func(lista,i)

    def salir(self,lista,i):
        print('Usted salio del programa')
    def opcion1(self,lista,i):
        lista.consultarMillas(i)


    def opcion2(self,lista,i):
        lista.acumularMilla(i)

    def opcion3(self,lista,i):
        lista.canjearMillas(i)

        
