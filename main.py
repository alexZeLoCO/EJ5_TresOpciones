n = int (input ("Introduzca un número entero: "))       #PIDE NÚMERO
    #TIPO INT
print ("Opción a) Cuadrado del número.")        #GUÍA USUARIO
print ("Opción b) Cubo del número.")            #GUÍA USUARIO
print ("Opción c) Doble del número.")           #GUÍA USUARIO

usr = input ("Opción: ")        #INPUT OPCIÓN
    #NO HAY TIPO ==> STR

if usr == "a":      #SI USR == A
    print ("El cuadrado del número",n,"es",n*n)     #OUTPUT
if usr == "b":      #SI USR == B
    print ("El cubo del número",n,"es",n*n*n)       #OUTPUT
if usr == "c":      #SI USR == C
    print ("El doble del número",n,"es",n*2)        #OUTPUT