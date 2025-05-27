# Bubble Sort ele faz comparaçoes de elementos que estao em posicoes consecutivas e troca eles se eles estiverem em ordem errada


def bubble_sort(lista):
    n = len(lista)
    for i in range(-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]


#facunciona bem em  listas pequenas e quase ordenadas. E pode para quando a lista estiver que quase ordenada


#realiza muitas trocas dependendo do tipo de lista, 

#como ele funciona? ele pega o primeiro elemento e compara se o valor dele e maior que o valor do proximo elemento, se for ele troca eles e vai para o proximo elemento.