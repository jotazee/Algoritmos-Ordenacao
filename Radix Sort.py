





def countingSortPorDigito(lista, exp):
    n = len(lista)  # Tamanho do array
    output = [0] * n  # Lista temporária para armazenar a ordenação parcial
    count = [0] * 10  # Lista de contagem para os dígitos de 0 a 9

    for i in range(n):      # Conta a ocorrência de cada dígito na posição atual (exp)
        indice = (lista[i] // exp) % 10  # Extrai o dígito atual
        count[indice] += 1  

    for i in range(1, 10):   # Atualiza a contagem acumulada para saber as posições corretas
        count[i] += count[i - 1]

    # Constrói a saída ordenada com base no dígito atual (do fim para o início, para estabilidade)
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        output[count[indice] - 1] = lista[i] 
        count[indice] -= 1 
        i -= 1  

    for i in range(n):          # Copia a ordenação parcial de volta para a lista original
        lista[i] = output[i]

# Função principal do Radix Sort
def radix_sort(lista):
    max_val = max(lista)     # Encontra o maior número na lista (para saber o número de dígitos)

    exp = 1         # Representa a posição do dígito (1 = unidade, 10 = dezena, 100 = centena, etc.)
    while max_val // exp > 0:
        countingSortPorDigito(lista, exp)       # Ordena os elementos com base no dígito atual
        exp *= 10                               # Move para o próximo dígito (da direita para a esquerda)