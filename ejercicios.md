# Ejercicios

## 01 - Suma con IVA

Escribe un programa que calcule la suma de dos cantidades (3) y (7) Y les aplique el IVA (21%)

Muestra al usuario el resultado de la operación


## 02 - Condicional:

Dado el programa anterior:

- Si el PVP es menor a 100 imprime
    - "Vamos a comprarlo"
- En caso contrario imprime
    - "No podemos permitirnoslo"

## 03 e.control

- Escribe código que haga la cuenta atrás de un cohete

ej:

```
10
9
8
7
6
5
4
3
2
1
DESPEGUE!
BROOOOOOOMMMMMM
---------------
```
## 04 - Funciones

Resuelve estos ejercicios usando funciones

- Muestra por pantalla el saludo `¡Hola amiga!` cada vez que se la invoque.
- Escribir una función a la que se le pase una cadena `<nombre>` y muestre por pantalla el saludo `¡hola <nombre>!.`
- Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
- Escribir una función que reciba un número entero positivo y devuelva su factorial.

```
ej de factorial:
    4! => 4·3!
    3! => 3·2!
    4! => 4·3·2·1
    4! => 24
```

```python
def factorial(numero):
    pass

numero = 4
resultado = factorial(numero)
print("El factorial de {numero} es {resultado}")
```

## 05 Casteo

Escribe una funcion recursiva que devuelva un numero entero
La función pedira al usuario el dato una y otra vez hasta que introduzca un num válido

## FizzBuzz

Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:

- Múltiplos de 3 por la palabra "Fizz".
- Múltiplos de 5 por la palabra "Buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "FizzBuzz".

## HTTP

Arregla el método camion del servidor flask
- Acepta y muestra 3 parametros URL: ruedas, color y peso
- El servidor NO debe fallar si faltan alguno (o todos) de los parametros
