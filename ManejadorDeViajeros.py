import csv
from claseViajeroFrecuente import ViajeroFrecuente
class ListaViajeros:

    def __init__(self):
        self.__lista=[]


    def AgregarViajero(self,viajero):
        self.__lista.append(viajero)

    def Inicializar (self):
        archivo=open("ViajerosFrecuentes.csv")
        reader= csv.reader(archivo,delimiter=";")
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                numero= fila[0]
                dni= fila[1]
                nom= fila[2]
                ape= fila[3]
                millas= fila[4]
                unViajero=ViajeroFrecuente(numero,dni,nom,ape,millas)
                self.AgregarViajero(unViajero)
        archivo.close()

    def __str__(self):
        s=""
        for viajero in self.__lista:
            s += str(viajero)+'\n'
        return s

    def buscarViajero(self,num):
        i=0
        unViajero=self.__lista[i]
        unNum=unViajero.getNumero()
        while((num!=unNum)and(int(i)<9)):
            i+=1
            unViajero=self.__lista[i]
            unNum=unViajero.getNumero()
        if i<11:
            print("Se encontro el viajero")
            print(unViajero)
            return i




    def consultarMillas(self,i):
        print("La cantidad de millas son "+str(self.__lista[i].getMillas()))

    def acumularMilla(self,i):
        m= input("Ingrese la cantidad de millas a acumular >> ")
        unViajero=self.__lista[i]
        unViajero.acumularMillas(m)

    def canjearMillas(self,i):
        m=input("Ingrese cantidad de millas a canjear >> ")
        unViajero=self.__lista[i]
        unViajero.canjearMillas(m)







