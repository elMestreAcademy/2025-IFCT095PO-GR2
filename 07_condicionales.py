a = 1
b = 2

print(a == b)             # False
print(a != b)             # True
print(a > b)              # False
print(a < b)              # True
print(a >= b)             # False
print(a <= b)             # True

x = 7

# and or not
#                         x [ 0 | 1 | 3.5 | 4.5 | 6  | 9 | 10    ]
x < 5 and x < 10	      # [              True | False          ]
x < 4 or x > 9.5          # [        True |     False    | True  ]
not(x < 5 and x < 10)     # [             False | True           ]

x < 4 or not x > 9.5      # [                       True | False ]
x < 4 or    x <= 9.5      # [                       True | False ]

x > 1 or x < -5 and x != 7.14

"""

CASTEO A BINARIO

  5 binario = 00000101   bool() => True
127 binario = 01111111   bool() => True
-64 binario = 10101011   bool() => True
  0 binario = 00000000   bool() => False

 "a"      : True
 "Patata" : True
 ""       : False
"""
