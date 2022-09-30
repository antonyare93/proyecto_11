class DivisiónPorCero(ZeroDivisionError):
    '''La división por cero(0) no está definida'''

def sumar(*args: int):
    resultado = 0
    for numeros in args:
        resultado += int(numeros) 

    return resultado

def restar(*args: int):
    resultado = 0
    for numeros in args:
        if numeros == args[0] and resultado == 0:
            resultado += int(numeros)
        else:
            resultado -= int(numeros)

    return resultado

def multiplicar(*args: int):
    resultado = 0
    for numeros in args:
        if numeros == args[0] and resultado == 0:
            resultado += int(numeros)
        else:
            resultado *= int(numeros)

    return resultado

def dividir(*args: int):
    resultado = 0
    for numeros in args:
        if numeros == args[0] and resultado == 0:
            resultado += int(numeros)
        elif not int(numeros) == 0:
            resultado /= int(numeros)
        else:
            print('La división por cero(0) no está definida')
            continue

    return resultado