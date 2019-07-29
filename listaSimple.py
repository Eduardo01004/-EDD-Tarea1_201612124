class Nodo:
    def __init__(self, dato=None, sig=None):
        self.dato = dato
        self.sig = sig

    def __str__(self):
        return "%s " %(self.dato)

class ListaSimple:
    def __init__(self):
        self.primero=None
        self.ultimo=None


    def Agregar(self, nuevo):
        nuevo = Nodo(dato)

        if self.primero==None:
            self.primero=nuevo
            nuevo.sig=None
            self.ultimo=self.primero
        else :
            self.ultimo.sig=nuevo
            nuevo.sig=None
            self.ultimo=nuevo


    def Listar(self):
        actual=self.primero
        while actual != None:
            print("********")
            print(actual)
            actual=actual.sig

    def Eliminar(self,elemento):
        actual=self.primero
        anterior=None
        while (actual!=None):
            if actual.dato==elemento:
                if actual.dato==elemento:
                    if actual==self.primero:
                        self.primero=self.primero.sig
                    elif actual==self.ultimo:
                        anterior.sig=None
                        self.ultimo=anterior
                    else :
                        anterior.sig=actual.sig
                print ("eliminado")
            anterior=actual
            actual=actual.sig

    def Modificar(self, dato,elemento):
        if self.primero.dato == dato:
            elemento.sig=self.primero.sig
            self.primero=elemento
            return True
        else:
            aux=self.primero
            anterior=aux
            while(aux!=None):
                if aux.dato==dato:
                    elemento.sig=aux.sig
                    anterior.sig=elemento
                    return True
                anterior=aux
                aux=aux.sig
        return False



    def menu(self):
    	print ("Selecciona una opción")
    	print ("\t1 - Agregar")
    	print ("\t2 - Listar")
    	print ("\t3 - Modificar")
    	print ("\t4 - Eliminar\n"+
               "\t5 - Salir")


if __name__=="__main__":
    lista=ListaSimple()
    bandera=True
    while (bandera):
        lista.menu()
        opcion=input("Selecciona una opción: ")
        if opcion=="1":
            dato = input("ingrese dato: ")

            lista.Agregar(dato)
        elif opcion=="2":
            lista.Listar()
        elif opcion == "3":
            dato1 = input("ingrese dato a buscar: ")
            datos=input ("ingrese nuevo dato ")
            nod=Nodo(datos)
            lista.Modificar(dato1,nod)

        elif opcion == "4":
            dato = input("ingrese dato: ")
            lista.Eliminar(dato)
        elif opcion == "5":
            bandera=False
