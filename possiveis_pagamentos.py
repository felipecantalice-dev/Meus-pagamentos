from itertools import combinations

def encontrar_possiveis_pagamentos(valores, k):
    possibilidades = []

    for i in range(len(valores) + 1):
        for combo in combinations(valores, i):
            if sum(combo) == k:
                possibilidades.append(combo)
    return possibilidades


if __name__ == '__main__':
    valores = [12.0, 3.0, 2.5, 7.0, 6.0, 1.0, 5.0]
    k = 10.0
    possibilidades = encontrar_possiveis_pagamentos(valores, k)
    print("Os possiveis pagamentos:")
    for possibilidade in possibilidades:
        print(possibilidade)