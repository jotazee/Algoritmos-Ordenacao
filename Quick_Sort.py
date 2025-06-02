
# Quick Sort ele escolhe um elemento da lista(pivo) e particiona a lista para que os menores fiquem para a esquerda e os maiores para a direita

#[4,7,2,6,4,1,8,3] escolher um pivo que sera o numero 3
#[4,7,2,6,4,1,8,3] como 4 e 7 são maiores que o pivo ele vai para a direita 
#[2,7,4,6,4,1,8,3] como 2 é menor que o pivo ele vai para a esquerda
#[2,4,7,6,4,1,8,3] como 1 eh menor que o pivo ele vai para a esquerda
#[2,1,4,6,4,7,8,3] como 6 eh maior que o pivo ele vai para a direita
#[2,1,3,6,4,7,8,4] como 3 eh menor que o pivo ele vai para a esquerda assim ficando no seu devido lugar
# agora que ja temos o pivo em seu lugar ele vai dividir a lista(como ele ja percorreu ele ja separou a lista ele sabe que na esquerda estao os menores e na direita os maiores)
# logo vai chamar o algoritmo novamente para ordenar a sublista
#[1,2,3,4,4,7,8,6] e assim vai ate acabar as posicoes
#[1,2,3,4,4,6,8,7] 
#[1,2,3,4,4,6,7,8]

def quicksort(lista, inicio=0, fim=None):# indica o inicio e o fim da lista
    if fim is None: #se o fim for fazio
        fim = len(lista)-1 # o fim sera o tamanho da lista menos 1 porque usamos o indice como pivo
    if inicio < fim: # se o inicio for menor que o fim
        p = partition(lista, inicio, fim)  # ter a posicao do pivo
        
        quicksort(lista, inicio, p-1) # calcular a posicao do pivo
        
        quicksort(lista, p+1, fim) #chmar o algoritmo novamente na sublista

def partition(lista, inicio, fim): #funcao para calcular a posicao do pivo
    pivot = lista[fim] # o pivo sera o ultimo elemento
    i = inicio # o i sera o primeiro elemento
    for j in range(inicio, fim): # percorrer a lista com a variavel j que vai percorrer a lista
        if lista[j] <= pivot: # faz uma comparacao com o pivo
            lista[j], lista[i] = lista[i], lista[j] #faz a troca de posicao
            i = i + 1 # incrementa o i
    lista[i], lista[fim] = lista[fim], lista[i] # troca de posicao
    return i



# e um agoritmo muito lento para listas grandes pois ele vai dividir a lista para que os menores fiquem para a esquerda e os maiores para a direita ele vai demorar dependendo da escolha  do seu pivor. isso pode requer mais memoria e processamento
# mas se a lista é pequena ele vai ser bem eficiente. pois ele vai divir a lista para que os menores fiquem para a esquerda e os maiores para a direita 