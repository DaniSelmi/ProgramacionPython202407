def ingreso_numero_entero(msg = 'Ingres un numero entero: '):
    try:
        numero = int(input(msg))
        return numero
    except ValueError:
        print('Por favor, ingrese un numero entero valido ...')
        return ingreso_numero_entero(msg)
    

def 