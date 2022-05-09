class ViajeroFrecuente:
    __num_viajero=0
    __dni=""
    __nombre=""
    __apellido=""
    __millas_acum=0

    def __init__(self,num,dni,nombre,apellido,millas):

        self.__num_viajero=num
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__millas_acum=int(millas)

    def getNumero(self):
        return self.__num_viajero

    def getMillas(self):
        return self.__millas_acum

    def cantidadMillasAcumuladas(self):
        return self.__millas_acum

    def acumularMillas(self,cant):
        self.__millas_acum +=int(cant)

    def canjearMillas(self,cantCanjear):
        if (self.__millas_acum>=int(cantCanjear)):
            print("Se pueden canjear las millas")
            self.__millas_acum-=int(cantCanjear)
        else:
            print("No se pueden canjear las millas")


    def __str__(self):
        return ("numero de viajero "+ self.__num_viajero + " DNI "+self.__dni+" Nombre del viajero "+self.__nombre+" Apellido del viajero "+ self.__apellido+ " Millas acumuladas "+ str(self.__millas_acum) )
