# ideia do algoritmo e inserir o elemento na posicao correta

#[4,7,2,5,4,0] 
#[4] se fosse uma lista com a penas um elemento ele seriaja estaria ordenado. mas vamos adicionar um novo elemento
#[4,7] como 7 e maior que 4 ja esta ordenado
#[2,4,7] inserimos o 2 na posicao correta 
#[2,4,5,7] inserimos o 5 na posicao correta
#[0,2,4,5,7] inserimos o 0 na posicao correta
#[0,2,4,4,5,7] inserimos o 4 na posicao correta
#[0,2,4,4,5,7] ja esta ordenado





def insertion_sort(lista):
    n = len(lista) #tamanho da lista
    for i in range(1, n): # percorre a lista integrando o elemento na posicao correta
        chave = lista[i] # chave diz quem esta na posicao i
        j = i - 1  # comeca no i menos um
        while j >= 0 and lista[j] > chave: #integrando
            lista[j+1] = lista[j] # equanto o J for maior avanca e se o J for maior que a chave
            j = j - 1
        lista[j+1] = chave


# para uma lista e pequena ele vai ser bem rapido vai exigir pouco processamento
# para uma lista grande ele vai ser lento vai exigir muito processamento e ficando lento a verificação dos elementos, assim perdendo muito tempo pois ele vai inserindo os 
# nas posicoes certas