"""las funciones del menu"""
"""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.4
fecha: 13/06/2024

"""
import colorama as color
import os


def parametrizar(lista):#vacia la lista del menu 
    lista.clear()
    
    
def registroAprendiz(lista,diccionario):
    i=0
    while i <=1:# creamos un ciclo while para controlar las veces que quiera el usuario registrar
        pregunta=input("desea registrar otro aprendiz (si o no)")
        if pregunta == "si":
            while True:#ciclo while para controlar los input sean de datos correctos
                documento= input("ingrese el documento: ")
                if documento.isdigit():
                    doc=str(documento)
                    print ("documento vale:", doc)
                    break
                else:
                    print("ingrese un valor numerico")
            while True:
                entrada= input("ingrese el nombre completo: ")#solicitamos el nombre
                if entrada.istitle():
                    nombre= str(entrada)
                    print("nombre completo",nombre)
                    break
                else:
                    print("Escriba correctamente el nombre completo")
            while True:
                entrada= input("ingrese la ficha: ")#solicitamos la ficha
                if entrada.isdigit():
                    ficha=str(entrada)
                    break
                else:
                    print("ingrese un valor numerico")   
            while True:
                entrada= input("ingrese la evaluacion digite 1= aprobo o 2= desaprobo: ")#solicitamos la evaluacion
                if entrada == "1":
                    evaluacion= "A"
                    break
                elif entrada == "2":
                    evaluacion= "D"
                    break
                else:
                    print("ingrese un valor correcto") 
                    #llegamos un diccionario con los datos ingresados
            diccionario={
            'documento': doc,
            'nombre': nombre,
            'ficha': ficha,
            'evaluacion': evaluacion,
            }
            lista += [diccionario]#agregamos el diccionario a la lista
        elif pregunta == "no":
            print("Regresando al Menu")
            i +=3
        else:
            print("escriba una opcion valida")
     
                 
def buscarLista(lista):
    if not lista: #verificamos que la lista no este vacia 
        print("No hay datos para mostrar")
        return
    #ubicamos las claves de la lista par generar la tabla
    claves = set(clave for aprendiz in lista for clave in aprendiz.keys())
    
    #sacamos el espacio mayor de las claves para que ningun valor este fuera de la tabla que se va a graficas
    #max(len(str(clave))) saca la cantidad de valores que hay en cada palabra y lo retorna en un numero
    espacioClave= max(len(str(clave)) for clave in claves)
    espacioValor= max(len(str(aprendiz[clave])) for aprendiz in lista for clave in claves
                                                if clave in aprendiz)

    print(f'{'clave':<{espacioClave}} | {'valor':<{espacioValor}}')#imprimimos el encabezado de la tabla con los espacios

    for aprendiz in lista: #for por cada aprendiz con un print que genera las separacion en cada aprendiz en la tabla
        print("-"*20)
        for clave in claves:#hacermos un for con otro for para a los valores de cada diccionario y los imprimimos 
            valor= aprendiz.get(clave, '') #obtiene el valor de la clave del deccionario en caso de que este vacio impime''
            print(f"{clave:<{espacioClave}} | {str(valor):<{espacioValor}}")


def listaFichas(lista):
     #recorremos las fichas con un for y guardamos dentro de una lista las fichas que se encuentren
     fichas = [aprendiz['ficha']for aprendiz in lista if 'ficha' in aprendiz ]

     unicasFichas= set(fichas)#sacamos los valores repetidos con la funcion set

     print("unicas fichas que existen:")
     print("se imprimen a continuacion")
     
     for i in unicasFichas:#con un for imprimimos las fichas
         print("-"*30)
         print("Estudiantes de la ficha: ",i)
         fichas= [aprendiz for aprendiz in lista if aprendiz.get('ficha') == i]
         buscarLista(fichas)
         os.system("pause")
             
     
     


def aprendicesFicha(lista):
    while True:#while para controlar las veces que el usuario va a ejecutar esa funcion
        #recorremos las fichas con un for y guardamos dentro de una lista las fichas que se encuentren
        fichas = [aprendiz['ficha']for aprendiz in lista if 'ficha' in aprendiz ]

        unicasFichas= set(fichas)#sacamos los valores repetidos con la funcion set

        print("unicas fichas que existen:")
        for i in unicasFichas:
            print(i)
        
        ficha = input("escriba el numero de la ficha que quiera buscar(solo numeros)o escriba 0 para salir")
        
        if ficha.isdigit() :
            busqueda= [aprendiz for aprendiz in lista if aprendiz.get('ficha') == ficha]#ubica el numero de la ficha ingresada y lo guarda en una lista
            if busqueda:
                print("aprendices con número de ficha", ficha, "\n")
                if not busqueda: #verificamos que la lista no este vacia 
                    print("No hay datos para mostrar")
                    return
                
                #ubicamos las claves de la lista par generar la tabla
                claves = set(clave for aprendiz in busqueda for clave in aprendiz.keys())
                
                #sacamos el espacio mayor de las claves para que ningun valor este fuera de la tabla que se va a graficas
                #max(len(str(clave))) saca la cantidad de valores que hay en cada palabra y lo retorna en un numero
                espacioClave= max(len(str(clave)) for clave in claves)
                espacioValor= max(len(str(aprendiz[clave])) for aprendiz in busqueda for clave in claves
                                                            if clave in aprendiz)

                print(f'{'clave':<{espacioClave}} | {'valor':<{espacioValor}}')#imprimimos el encabezado de la tabla con los espacios
                
                
                for aprendiz in busqueda: #for por cada aprendiz con un print que genera las separacion en cada aprendiz en la tabla
                        print("-"*20)
                        for clave in claves:#hacermos un for con otro for para a los valores de cada diccionario y los imprimimos 
                            valor= aprendiz.get(clave, '') #obtiene el valor de la clave del deccionario en caso de que este vacio impime''
                            if aprendiz.get('evaluacion') == 'A':
                                print(color.Fore.GREEN + f"{clave:<{espacioClave}} | {str(valor):<{espacioValor}}"+ color.Style.RESET_ALL)#imprimimos en pantalla si aprobo en color verde
                            else:
                                print(color.Fore.RED + f"{clave:<{espacioClave}} | {str(valor):<{espacioValor}}"+ color.Style.RESET_ALL)#imprimimos en pantalla si desaprobo en rojo
                
                #buscarLista(busqueda)#se llama a la funcion buscar lista para imprimir los aprendices de esa ficha 
            elif ficha == "0":
            
                print("regresando al menu")
                break   
        else:
                print("numero de ficha no encontrado")#en caso de que no se encuentre la ficha 


def borrarAprendiz(lista):
        while True:#ciclo para controlar las veces que el usuario va a ejecutar esa funcion
            preguntar= input("¿desea borrar un aprendiz?(si/no)").lower()
            if preguntar =="si":
                buscarLista(lista)
                documento = input("escriba el numero del documento que quiera BORRAR(solo numeros)o escriba 0 para salir")
                if documento.isdigit():#aseguramos que el documento ingresado sea numero 
                    buscar= [aprendiz for aprendiz in lista if aprendiz.get('documento')== documento]#buscamos el documento en la lista
                    if buscar:
                        for aprendiz in buscar:#recorremos la lista para ubicarnos en el aprendiz que vamos a eliminar
                            lista.remove(aprendiz)#eliminamos el aprendiz con el domuneto
                            print("EL APRENDIZ FUE ELIMINADOOOOOO")
                    elif documento == "0":
                    
                        print("regresando al menu")
                        break
                    
                    else:
                        print("no se encontro el documento")
                
                else:
                    print("escriba una opcion valida")
            elif preguntar == "no":
                documento= "0"
                break
            else:
                print("escoga un opcion valida")


def actualizarInfo(lista):
     while True:#ciclo para controlar las veces que el usuario va a ejecutar esa funcion
        preguntar= input("¿desea actualizar un aprendiz?(si/no)").lower()
        buscarLista(lista)
        if preguntar =="si":
            documento = input("Ingrese el documento del registro que desea actualizar: ")#solicitamos el documento del aprendiz que se va a actualizar
            if documento:#aseguramos que sea un valor numerico
                registro_encontrado = next((aprendiz for aprendiz in lista if aprendiz['documento'] == documento),None)#lo buscamos en la lista y nos ubicamos en ese diccionario,
                                                                                                                        #en caso contrario regresamos un none
                if registro_encontrado:
                    #le preguntamos que campo a actualiar
                    campo = input("Ingrese el campo que desea actualizar (nombre, ficha, evaluacion): ").lower()
                    if campo in registro_encontrado:
                        if campo == 'documento': # aseguro que el documento no se pueda modificar
                            print("el documento no se puede actualizar")
                            break
                        elif campo == 'evaluacion':
                            while True:
                                entrada= input("ingrese la evaluacion digite 1= aprobo o 2= desaprobo: ")
                                if entrada == "1":
                                    nuevo_valor= "A"
                                    registro_encontrado[campo] = nuevo_valor#aqui se actualiza los datos segun lo ingresado
                                    #imprimimos el cambio realizado(el .capitalize es para imprimir la primera letra del campo en mayuscula)
                                    print(f"{campo.capitalize()} actualizado correctamente.")
                                    break
                                elif entrada == "2":
                                    nuevo_valor= "D"
                                    #aqui se actualiza los datos segun lo ingresado
                                    registro_encontrado[campo] = nuevo_valor
                                    #imprimimos el cambio realizado(el .capitalize es para imprimir la primera letra del campo en mayuscula)
                                    print(f"{campo.capitalize()} actualizado correctamente.")
                                    break
                                else:
                                    print("ingrese un valor correcto") #en caso de que ingrese un valor erroneo
                        else:
                                while True:
                                    nuevo_valor = input(f"Ingrese el nuevo valor para {campo}: ")#solicito el dato que puede ser de la ficha  el nombre
                                    if  campo == 'ficha':
                                        if nuevo_valor:#aseguramos que el valor ingresado sea digito
                                            nuevo_valor = str(nuevo_valor)#aseguramos mas aun que el valor sea numerico y entero
                                            registro_encontrado[campo] = nuevo_valor#remplazamos el valor antiguo con el nuevo
                                            #imprimimos el cambio realizado(el .capitalize es para imprimir la primera letra del campo en mayuscula)
                                            print(f"{campo.capitalize()} actualizado correctamente.") 
                                            return True
                                        else:
                                            print("digite un valor numerico")   
                                    elif nuevo_valor.istitle():#me aseguro que el nombre sea escrito correctamente
                                        registro_encontrado[campo] = nuevo_valor#actualiza el valor(en este caso el nombre)
                                        #imprimimos el cambio realizado(el .capitalize es para imprimir la primera letra del campo en mayuscula)
                                        print(f"{campo.capitalize()} actualizado correctamente.")
                                        return True
                                    else:
                                        print("digite el nombre correctamente")#en caso de que ingrese un valor erroneo        
                    else:
                        print("Campo no encontrado.")#en caso de que no se encuentre el campo
                else:
                    print("Documento no encontrado")#en caso de no se encuentre el documento
            else:
                print("Digite un valor numerico")#en caso de que ingrese un valor erroneo
        elif preguntar == "no":
            documento= "0"
            break
        else:
            print("escoga un opcion valida")



            

            

                