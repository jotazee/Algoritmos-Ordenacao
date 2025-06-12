# Merge Sort separa a lista em partes menores e depois junta as partes ordenando elas(não é um algoritmo muito intuitivo)
# [4,7,2,6,4,1,8,3] vai dividir a lista pela metade
#[4,7,2,6] [4,1,8,3] ele sempre vai separa pois o algoritmo acha que nao pode resolver o problema. ele sempre vai querer um problema menor
#[4,7] [2,6] [4,1] [8,3] 
#[4] [7] [2] [6] [4] [1] [8] [3] agora estao tudo em sublistas menores
#agora ele vai juntar as sublistas comparando os elementos para ver qual o menor e colocando na lista principal
# lista ordenada
#[2,4,6,7] [1,3,4,8] agora ele vai juntar as sublistas comparando os elementos para ver qual o menor e colocando na lista principal
# [1,2,3,4,4,6,7,8]fim do algoritmo


def mergesort(lista, inicio=0, fim=None): # usando parametros
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):#se o fim for maior que o inicio (porque se for mais do q 1 ele vai dividir a lista)
        meio = (fim + inicio)//2 # vai dividir a lista em 2
        mergesort(lista, inicio, meio) # recursao lado esquerdo
        mergesort(lista, meio, fim) # recursao lado direito
        merge(lista, inicio, meio, fim) # ele vai juntar as sublistas comparando os elementos para ver qual o menor e colocando na lista principal

def merge(lista, inicio, meio, fim): # 
    left = lista[inicio:meio] # metade esquerda
    right = lista[meio:fim] # metade direita
    top_left, top_right = 0, 0 # variaveis auxilia para pecorrer o topo das sublistas
    for k in range(inicio, fim): # vai pecorrer a lista principal
        if top_left >= len(left): # verifica se o topo da metade esquerda chegou ao fim
            lista[k] = right[top_right] #o que estiver na metade direita vai para a lista principal
            top_right = top_right + 1
        elif top_right >= len(right): # caso ao contrario o que estiver na metade esquerda vai para a lista principal
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]: # se o topo da metade esquerda for menor que o topo da metade direita
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right] # se o topo da metade direita for menor que o topo da metade esquerda
            top_right = top_right + 1


# para uma lista grande ele pode ate ser bem eficiente porem ele vai demorar e vai usar muito espaco de memoria
# ja para lista pequena ele nao funciona bem pelo nivel de complexidade do algoritmo ele caba dividino demais as sublistas
# pode ser usado para ordenar listas grandes.