# O countig e um algoritmo de ordenação que utiliza o conceito de contagem para classificar elementos em uma lista.

# [4, 2, 2, 8, 3, 3, 1]
# [0, 1, 2, 2, 1, 0, 0, 0, 1] cria um vetor de contagem
# [0, 1, 3, 5, 6, 6, 6, 6, 7] faz uma soma
# [1, 2, 2, 3, 3, 4, 8] resultado final


def counting_sort(arr):
 
    max_val = max(arr)
    min_val = min(arr)
    range_of_values = max_val - min_val + 1

    
    count = [0] * range_of_values
    output = [0] * len(arr)

    
    for num in arr:
        count[num - min_val] += 1

  
    for i in range(1, len(count)):
        count[i] += count[i-1]

    
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output



# muito bom para contagens de frequencias dos elementos
# porem para uma ordenacao nao muito eficiente pois necessita de espaco adicional isso requer memoria 