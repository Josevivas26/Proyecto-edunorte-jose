#Reglas generales de las funciones:
#1- no se ejecuta la funcion a menos que la llames
#2- la puedo llamar la cantidad de veces que quiera
#3- primero hay que definir la funcion, y despues llamarla
#4- primero van los parametros requeridos, y al final los opcionales
#5- para cambiar el scope de una variable, utilizar return

#FUNCIONES SIN PARAMETROS
#def miFuncion():
    #conjunto de instrucciones

def derechos_humanos():
    d1="Derecho a la vida"
    d2="Derecho a la igualdad ante la ley"
    d3="Derecho a la libertad"

derechos_humanos()

def derechos_mayorDeEdad():
    d4="Derecho a votar"
    d5="Derecho al trabajo"

def mayoria_de_edad(nombre,edad):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()

def mayoria_de_edad2(edad,nombre='DESCONOCIDO'):
    print(f'Según la edad de {nombre}, sus derechos son:')
    if edad >= 18:
        derechos_humanos()
        derechos_mayorDeEdad()
    else:
        derechos_humanos()


#seleciona el importe
if __name__=="__main__" :
    mayoria_de_edad()
    mayoria_de_edad2()
