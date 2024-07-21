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

# 2. Definir las constantes


# 4. Deifinimos la función princial
def main():
    while True:
        print( """Bienvenido al menú interactivo
        Qué quieres hacer? Escribe una opción
        1) Saludar
        2) Calcular el factorial de un numero
        3) Calcular el area de un circulo
        4) Suma de divisiores de un numero
        5) Generar un triangulo rectangulo
        6) Salir""")

        opcion = input() # me devuelve un string
        if opcion == '1':
            print("Hola, espero que te lo estés pasando bien")

        elif opcion == '2':
            n = float(input("Introduce el factorial de un número: "))
            resultado = 1
            for i in range(1, n + 1):
                resultado *= i
            print(f"El resultado del factorial de {n}: {resultado}")

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
            print("¡Hasta luego! Ha sido un placer ayudarte")
            break

        else:
            print("Comando desconocido, vuelve a intentarlo")

        pass

    # 5. Punto de entrada a la aplicacion
    if __name__ == '__main__':
        main()





