#Crie um dicionário dos primeiros  100  números primos com a chave sendo o número primo
#  e valor a raíz quadrada do número primo.
#Observação: use dict[key] = novo_valor

from math import sqrt

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primos_raiz = {}
for numero in numeros_primos:
    primos_raiz[numero] = sqrt(numero)