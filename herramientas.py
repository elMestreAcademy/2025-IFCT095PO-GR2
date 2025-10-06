"""
Escribe una funcion recursiva que devuelva un numero entero
Esto es el ejercicio 05 - Casteo
"""


def introduce_entero(msg="Introduce un dato: ", entero_positivo=False):
    str_entrada = input(msg)
    try:
        int_numero_entero = int(str_entrada)
    except ValueError:
        msg = " - ERROR: no es un entero válido\nIntroduce un entero válido: "
        int_numero_entero = introduce_entero(msg, entero_positivo)

    if entero_positivo and int_numero_entero < 0:
        msg = " - ERROR: no es un entero válido\nIntroduce un entero >= 0: "
        int_numero_entero = introduce_entero(msg, entero_positivo)

    return int_numero_entero


# Si estoy en el contexto princiupal ejecuto el ejemplo
if __name__ == "__main__":
    mi_numero = introduce_entero(entero_positivo=True)
    for i in range(mi_numero):
        print(f" ** {i}")
