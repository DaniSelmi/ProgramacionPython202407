"""
Generaremos un programa menu que realice las siguiente tareas.

1. Saludar
2. Calcular el factorial de un numero
3. Calcular el area de un circulo
4. Suma de divisiores de un numero
5. Generar un triangulo rectangulo
6. Salir
"""


# 1. Importamos Librerias
import math

# from <nombre_carpeta> import <nombre_archivo> as <nombre_corto>

##  from mate import funciones as mate

# import <nombre_archivo> as <nombre_corto>
#import validaciones ## FORMA 1

## FORMA 2
from validaciones import ingreso_numero_entero
from mate import areas

# 2. Definir las constantes
MENSAJE_BIENVENIDA = "Bienvenido al menú interactivo"
MENSAJE_OPCIONES = """¿Qué quieres hacer? Escribe una opción
1. Saludar
2. Calcular el factorial de un numero
3. Calcular el area de un circulo
4. Suma de divisiores de un numero
5. Generar un triangulo rectangulo
6. Salir

REPUESTA: """""

MENSAJE_SALIDA = "¡Hasta luego! Ha sido un placer ayudarte"

# 3. Definimos Funciones y/o claes
def saludar():
    print("Hola, espero que te lo estés pasando bien")

def factorial(numero):
    
    assert numero >= 0, "Debemos ingresar un numero positivo"
    
    if numero == 0 or numero ==1:
        return 1
    return numero * factorial(numero - 1)

def opcion_3()
    radio = ingreso_numero_entero("Ingresa el radio ...")
    
    #genero una excepcion si el radio es negativo
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")

    #Calculo el area del circulo
    area = areas.area_circulo(radio)



# 4. Deifinimos la función princial
def main():
    #Codigo de la funcion principal
    print(MENSAJE_BIENVENIDA)
    while True:
        #Mostrar las opciones del menu
        print(MENSAJE_OPCIONES)

        opcion = input() # me devuelve un string

        if opcion == '1':
            saludar()

        elif opcion == '2':
            numero = int(input ("Ingresa un número para calcular su factorial: "))

            factorial(numero)
            print(f"{numero}! = {numero}")

        elif opcion == '3':
            radio = float(input("Introduce el radio del círculo : "))
            area = math.pi * (radio ** 2)
            print(f"El resultado del área de un circulo con un radio de {n}: {area}")
        
        elif opcion == '4':
            numero = float(input("Introduce el número: "))
            suma = 0
            for i in range(1, numero + 1):
                if numero % i == 0:
                    suma += i
            print(f"El resultado de la suma de divisores de {numero}: {suma}")
        
        elif opcion == '5':
            numero = float(input("Introduce el número: "))
            for i in range(1, numero + 1):
                print('*' * i) 
        
        elif opcion == '6':
            print(MENSAJE_SALIDA)
            break

        else:
            print("Comando desconocido, vuelve a intentarlo")

        pass

    
# 5. Punto de entrada a la aplicacion
if __name__ == '__main__':
    main()

#Comando ayuda a que se ejecute solo el comando respectivo






