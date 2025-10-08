# TABLAS DE LA VERDAD

0 == False
1 == True

Y (AND)
voy a comprar una casa si:

- A: Tengo suficiente ahorro para la entrada
- B: Encuentro una buena oportunidad de compra

O (OR)
Yo voy cenar si:
- A: Tengo comida en la nevera
- B: Tengo dinero para pedir cena

## Operaciones binarias básicas

```
 A B AND   A B  OR
 0 0  0    0 0  0
 0 1  0    0 1  1
 1 0  0    1 0  1
 1 1  1    1 1  1

 A NOT     A B XOR
 0  1      0 0  0
 1  0      0 1  1
           1 0  1   
           1 1  0  
```

## Operaciones binarias combinadas

```
 A B NAND (NOT AND)
 0 0  1    
 0 1  1    
 1 0  1    
 1 1  0
```

## Bitwise 

    010101011010           010101011010
AND 100011101101        OR 100011101101
    000001001000           110111111111


    010101011010           010101011010
<<  101010110100       >>  001010101101

```
