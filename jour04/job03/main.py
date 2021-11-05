x = int(input("Entrer un nombre entier : "))
n = int(input("Entrer un nombre entier en exposant : "))


def exp_factorial(x, n):
    if n < 0:
        print("nombre negatif")
        return 1 / exp_factorial(x, -n)
    elif n == 0:
        print("n = 1")
        return 1
    else:
        print("n > 1")
        return x * exp_factorial(x, n-1)


print(exp_factorial(x, n))