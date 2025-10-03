def factorial(factor):
    if factor == 0:
        return 1

    contador = 1
    acumulado = 1

    while contador <= factor:
        acumulado = acumulado * contador
        contador += 1

    return acumulado


print(factorial(10))
