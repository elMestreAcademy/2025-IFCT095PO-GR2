def factorial(factor):
    if factor == 0:
        return 1
    else:
        return factor * factorial(factor - 1)


print(factorial(10))
