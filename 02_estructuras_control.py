"""
a = 5
b = 0
if b != 0:
    print(a / b)
else:
    print("No puedo dividir porque el dividendo es 0")
print("Después del if")
print("===============")

# IFs anidados

letter = "A"

if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter isn't A, B and C")

a = 7

if a < 5:
    print("suspendido")
elif a >= 10:
    print("matricula de honor")
elif a >= 7:
    print("notable")
elif a >= 6:
    print("bien")
else:
    print("aprobado")

"""

# While

a = 1                     # Operador de asiganación -- Dentro de a <= 1 guardamos

while a <= 10:             # Operador de igualdad -- Comparamos a con un 1 -- True, False
    print("Kowabunga", a)
    a += 1
