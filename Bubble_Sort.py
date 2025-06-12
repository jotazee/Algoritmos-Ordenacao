# bubble sort algortimo que faz comparação entre com elemento que esta em posicao consecutiva

#[4,9,2,1,7,8] comparando 4 com 9
#[4,9,2,1,7,8] comparando 9 com 2
#[4,2,9,1,7,8] comparando 2 com 1
#[1,2,4,9,7,8] comparando 1 com 7
#[1,2,4,7,9,8] comparando 7 com 8
#[1,2,4,7,8,9] comparando 8 com 9
#[1,2,4,7,8,9] ordenada


def bubble_sort(lista): 
    n = len(lista) # tamanho da lista
    for j in range(n-1): # faz a comparação 
        for i in range(n-1): 
            if lista[i] > lista[i+1]: # verifica se o primeiro elemento da lista e maior que o segundo
                aux = lista[i]
                lista[i], lista[i+1] = lista[i+1], lista[i] # troca o primeiro elemento pelo segundo


# agoritmo muito lendo para lista maiores pois ele vai adicionando e verificando se o elemento e maior ou menor que o proximo
# so funciona com listas pequenas