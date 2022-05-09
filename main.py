from claseViajeroFrecuente import ViajeroFrecuente
from ManejadorDeViajeros import ListaViajeros
from claseMenu import Menu

if __name__ == '__main__':

    lista=ListaViajeros()
    lista.Inicializar()
    print(lista)
    num=input("Ingrese un numero de viajero >> ")
    i=lista.buscarViajero(num)
    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 2.1: Consultar cantidad de millas")
        print("2 ITEM 2.2: Acumular las millas")
        print("3 ITEM 2.3: Canjear millas")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,lista,i)
        bandera = int(opcion)== 0
