# Meus pagamentos

Tendo uma lista de pagamentos a serem pagos, encontre todos os itens que estão contidos na lista, onde somados equivalem a um valor k, onde k é o que o pagador quer pagar.

![](images\screen1.png)

## Algoritmo
1. Iniciar um loop de i=0 até o tamanho da lista. 
2. Calcular todas as combinações possiveis $C_{lista, i}$.
3. Verificar a soma da combinação encontradad é igual ao valor k.
    * Se sim, adicione a lista de possibilidades