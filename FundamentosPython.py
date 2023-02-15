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

    nuevoTema("Enteros")
    w = 105
    x = 59539865396
    y = -345
    z = 0b101010101
    h = 0xffa

    print(w, type(w))
    print(x, type(x))
    print(y, type(y))
    print(z, type(z))
    print(h, type(h))

    nuevoTema("Flotantes")
    x = 1297.5
    y = 0.4532627
    print(x,type(x))
    print(y,type(y))

    nuevoTema("Numeros Complejos")
    x = -46j
    y = 12 + 45j
    z = 2j

    print(x, type(x))
    print(y, type(y))
    print(z, type(z))

    nuevoTema("Listas")
    a = [10, 20.5, "Python List"]
    print(a, type(a))
    a = ["lista2", 45, 16.3j]
    print(a)
    print(a[2])

    nuevoTema("Tuplas")
    t = (25, "tupla", 5.6) #Las Tuplas no se pueden modificar, una vez asignado, se quedan asi.
    print(t)
    print(t[1])

    nuevoTema("Conjuntos")
    c = {50,20,10,4,8,50}
    print(c)

    nuevoTema("Diccionario")
    d = {1:"Valor1","2":45}
    print(d,type(d))

    nuevoTema("Cadenas")
    cadena1 = "Cadena entre comillas dobles"
    cadena2 = 'Cadena entre comillas sencillas'
    cadena3 = '''Cadena
    de
    varias
    lineas
    '''
    print(cadena1)
    print(cadena2)
    print(cadena3)