#Esto es un comentario.

def nuevoTema(tema):
    print("\n=====",tema,"=====\n")

if __name__ == "__main__":
    nuevoTema("Operadoes Aritmeticos")
    print("Operador de división entera (10 // 3): ", 10//3)
    print("Operador de potencias (5^5): ", 5**5)
    print("Operador de cambio de signo (-5): ",-5)

    nuevoTema("Operadores Logicos")
    print("Operador and (True and False): ", True and False)

    nuevoTema("Operadores de comparacion")
    print("2==3",2==3)

    #Actividad: Mostrar las tablas de verdad de los operadores lógicos.

    nuevoTema("Variables")
    variable1=10
    variable2=34.2
    variable3="Pepe"
    variable4="Hola"
    variable5="Hello"
    print(variable1,variable2,variable3,variable4,variable5)

    a,b,c=98,3.1416,"Bienvenido"
    print(a,b,c)