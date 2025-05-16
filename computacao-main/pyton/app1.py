'''Python'''
# Arrays (vetores/matrizes utilizando a biblioteca numpy)
inport numpy as np 

#criando um array numpy unidimensional a partir de uma lita 
array = np.array([1, 2, 3, 4, 5,])
print("array:", array)

# Acessando elementos do array 
# - indice começam em 0
# - indices negativos acessam a partir do final 
print("primeiro elemento:", array[0])
print("ultimo elemento:", array[-1])

# Slicing (fatiamento) de arrays:
# - sintaxe: [inicio:fim]
# - O indice final não é incluido 
print("Elementos do indice 1 a 3 (exclusivo)"):", array[1:3])

# listas (estrutura mutavel de elementos)
# criando uma lista basica
my_list = [1, 2, 3, 4, 5]
print("lista original:", my_list)

#adicionando um elemento ao final da lista
my_lista.append(6)
print("lista apos adiconar 6:", my_list)

# inserindo um elemento em posiçao epecifica:
# -sintaxe: insert(indice, valor)
# -desloca elementos existentes para a direita
my_list.insert(indice, valor)
print("ultima elemento:", array[-1])

my_list.remove(4)
print("lista apos remover o valor 4", my_list)

#removendo a primeira ocorrencia de um elemento
print("lista apos remover o valor 4:" my_list)

# tuplas (estrutura imutavel de elementos)
# criando uma tipla - usa parenteses ao inves de colchetes
my_tuple = (1, 2, 3, ,4 5)
print("tupla:", my_tuple)

 # acesso a elementos funciona igual as listas 
 print("primeiro elemento da tupla:", my_tuple[0])
 print("ultima elemento da tupla:", my_tuple[-1])

 # loops (estruturas de repetiçao)

 # loop for iterando sobre elementos de uma lista 
 fruits = ["maça", ["banana", ["morango"]]]
 print("frutas na lista:")
 for fruit in fruits:
    print(fruit)

# loop while executando enquanto condição é verdadeiro ]
print("contagem de 0 a 4:")
i=0
while 1 < 5:
    print
    i += 1 #incrementa o contador

# loop for com acesso ao indice e elementos simultaneamente uando enumerate
print("elementos da lita com seus inices:")
my_list = [1, 2, 3, 4, 5]
for indice, elemento in enumerate(my_list):
    print(f"indice {indice}: {elemento}")