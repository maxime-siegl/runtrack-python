nb_reine = int(input("Entrer le nombre de reine à placer : "))


def plateau(n, m, solution):
    if n == 0:
        return
    else:
        print(nb_ligne(m, solution[n - 1]))

        return plateau(n-1, m, solution)


def nb_ligne(m, solution):
    ligne_tab = []
    while m > 0:
        if m - 1 == solution:
            ligne_tab.append('X')
        else:
            ligne_tab.append('O')

        m -= 1

    return ligne_tab


def postition_secure(col, reines):
    line = len(reines)
    return (not col in reines and
            not any(abs(col - x) == line - i for i, x in enumerate(reines)))


def solve(n):
    solutions = [ [] ]
    for row in range(n):
        solutions = [solution + [i] for solution in solutions
                    for i in range(n)
                    if postition_secure(i, solution)]
    print(solutions[0])
    return plateau(n, n, solutions[0])


solve(nb_reine)