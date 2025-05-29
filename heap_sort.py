def heap_sort(lista):
    n = len(lista)
    for i in range(n//2 - 1, -1, -1):
        heapify(lista, n, i)
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

def heapify(lista, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2
    if esq < n and lista[esq] > lista[maior]:
        maior = esq
    if dir < n and lista[dir] > lista[maior]:
        maior = dir
    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        heapify(lista, n, maior)