# Meus pagamentos

Tendo uma lista de pagamentos a serem pagos, encontre todos os itens que estão contidos na lista, onde somados equivalem a um valor k, onde k é o que o pagador quer pagar.

![Descrição do funcionamento](images\screen1.png)

## Algoritmo
1. Iniciar um loop de i=0 até o tamanho da lista. 
2. Calcular todas as combinações possiveis $C_{lista, i}$.
3. Verificar a soma da combinação encontradad é igual ao valor k.
    * Se sim, adicione a lista de possibilidades


```python
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
```