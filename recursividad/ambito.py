a = 0


def funcion1():
    a = 7
    print(a)


def funcion2():
    global a

    print(a)
    a += 2
    print(a)


def funcion3():
    global a

    a = 22
    print(a)
    funcion2()
    print(a)


funcion1()
funcion3()
print(f"AL FINAL LA a VALE {a}")
