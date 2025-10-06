def detalles(variable):
    print(variable, "-", type(variable))


a = int(3)
b = int(3.95)
c = int('33')
d = int('4')

detalles(a)
detalles(b)
detalles(c)

detalles(a + b)
detalles(c + d)
detalles(c + a)

print("resultado:")
resultado = int(round(3.8 / 2))
detalles(resultado)

print("Input:")
variable = input("Introduce la cantidad: ")
detalles(variable)

variable_entero = int(variable)
detalles(variable_entero)

variable_float = float(variable)
detalles(variable_float)
