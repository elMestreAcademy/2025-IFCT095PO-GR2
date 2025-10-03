MAX = 3


def decrementa(a):
    s = (MAX - a) * "·"
    print(s, "Empieza decrementa con", a)

    if a > 0:
        a -= 1
        print(s, a)
        decrementa(a)

    print(s, "Fin de funcion")


decrementa(MAX)
