import random
from Selection_Sort import selection_sort
from Bubble_Sort import bubble_sort

any_numbers = random.sample(range(1, 100), 20) # 20 números aleatórios

already_sorted = [1,2,3,4,5,6,7,8,9,20,22,23,28,32,34,76,39,40,42,87,99,112] # lista já ordenada

inversed = [117,90, 88, 83,81,77,74, 69, 64,63,51,50,49,42,39,35,34,31,30,29,28,27,26,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1] # lista invertida

repeated = [7,7,7,7,7,1,1,9,9,0,4,4,4,5,4,5,7,1] # lista com números repetidos


if __name__ == "__main__":
   lista = any_numbers
   print(lista)
   bubble_sort(lista)
   print(f"\n Lista Ordenada: {lista}") 