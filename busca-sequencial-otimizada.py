import random

# n eh o tamanho da sequencia
n = 9

#Busca sequencial
def busca_sequencial(vetor, chave):
    for i in range(n):
        if vetor[i] == chave:
            return i
    return -1


#declarando o vetor inicial e povoando ele com elementos aleatórios
vetor = []
for i in range(n):
    numero_aleatorio = random.randint(0,50)
    vetor.append(numero_aleatorio)


#ordenando o vetor antes de fazer a busca da(s) chave(s)
vetor.sort()

#declando a quantidade de buscas a serem realizadas
q = input("Digite quantas chaves vc quer buscar ")
q = int(q)

#declarando o vetor de chaves a serem buscadas no vetor inicial
vetor_de_chaves = []
for i in range(q):
    numero_aleatorio=random.randint(0,50)
    vetor_de_chaves.append(numero_aleatorio)

#fazemos as q buscas no vetor inicial
for i in range(q):
    indice = busca_sequencial(vetor, vetor_de_chaves[i])
    if indice == -1:
        print(f"a chave {vetor_de_chaves[i]} não foi encontrada")
    else:
        print(f"a chave {vetor_de_chaves[i]} foi encontrada no indice {indice}")
    indice = 0