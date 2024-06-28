"""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.4
fecha: 13/06/2024

"""
"""
Este codigo  de un menu manejado con diccionarios
tiene 7 funciones para manejar los datos de los diccionarios
"""
import os
import module.funcionesMenu as fm

os.system("cls")
#lista de prueba para ejecutar las funciones
lista=[{'documento': '123456','nombre': 'Kevin','ficha': '85', 'evaluacion': 'A'},{'documento': '546213','nombre': 'Donato','ficha': '85', 'evaluacion': 'D'},{'documento': '879546','nombre': 'Santiago','ficha': '88', 'evaluacion': 'A'} ]
aprendices={
    'documento':'',
    'nombre':'',
    'ficha':'',
    'evaluacion':'',
}

                
# la funcion "iniciar()" dara el comienzo al programa
def iniciar(): 
     texto="BIENVENIDOOOOO!!! :D"
     #centramos en texto de bienvenido"
     print( texto.center(80," "))    
     i=0
     while i <= 1:
        #print(lista)
         
        print( "menu de aprendizes que accion quieres realizar")
        print(  "\n","1- PARAMETRIZAR","\n",
                "2- REGISTRO APRENDIZ","\n",
                "3- LISTA DE APRENDIZES","\n",
                "4- CODIGOS DE FICHAS","\n",
                "5- APRENDIZES POR FICHA","\n",
                "6- BORRAR APRENDIZ","\n",
                "7- ACTUALIZAR INFORMACIÓN","\n",
                "0- SALIR")
        pregunta= input("Digite una opcion del menu (0-7)")[0:7]
        # en caso de que la respuesta sea si llama a la funcion que ejecutara el programa
        if pregunta == "1":
            fm.parametrizar(lista)
            print("la lista fue limpiada")
            #print(lista)
        # si la respuesta es "no"  se finalizara el proceso
        elif pregunta == "2":
            fm.registroAprendiz(lista, aprendices)
            #print(lista)
        elif pregunta == "3":
            fm.buscarLista(lista)
        elif pregunta == "4":
            fm.listaFichas(lista)
        elif pregunta == "5":
            fm.aprendicesFicha(lista)
        elif pregunta == "6":
            fm.borrarAprendiz(lista)
        elif pregunta == "7":
            fm.actualizarInfo(lista)
        
        elif pregunta == "0":
            print("cerrando maquinaria bai")
            i +=3
        # si la respuesta esat fuera de las opciones se enviara  un mensaje de error
        else:
            print("escriba una opcion valida")

          
# llamamos a la funcion iniciar() para comenzar
if __name__=="__main__":
    iniciar()