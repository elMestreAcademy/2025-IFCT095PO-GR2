texto = "56"
print(texto, type(texto))

numero = int("56")
print(numero, type(numero))

try:
  a = 3/0
except:
  print(">>>>  An exception occurred  <<<<")
  a = "Patata"
  print(f"Guardamos \"{a}\" en la a")

try:
    texto += 1
except:
   print("WARNING: no se puede incrementar debido a incompatibilidad de tipos")
   print("RESETEANDO LA CUENTA")
   texto = 0

print(texto, type(texto))

numero += 1
print(numero, type(numero))
