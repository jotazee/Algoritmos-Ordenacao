#selection sort olha uma lista de dados e procurar o elemento maior ou menor e colocar ele no final da lista ou no inicio da lista

lista = [7, 5,1,8,3]

def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j]> lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
        
  