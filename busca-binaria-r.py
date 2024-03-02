import random

# n é o tamanho da sequencia
n = 9

#Busca binária com recursividade
def busca_binaria_recursiva(vetor, inicio, fim, chave):
    #caso base para limitar a recursividade da função
    if fim >= inicio:
        meio = (inicio + fim)//2
        meio = int(meio)

        if vetor[meio] == chave:
            return meio
        #caso onde a chave se existir está na metade à esquerda do vetor
        elif vetor[meio] > chave:
            return busca_binaria_recursiva(vetor, inicio, meio-1, chave)
        #caso onde a chave se existir está na metade à direita do vetor
        else:
            return busca_binaria_recursiva(vetor, meio+1, fim, chave)    
    else:
        return -1

#declarando o vetor inicial e povoando ele com elementos aleatórios
vetor = []
for i in range(n):
    numero_aleatorio = random.randint(0,50)
    vetor.append(numero_aleatorio)

#ordanação do vetor
vetor.sort()

print(vetor)

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
    indice = busca_binaria_recursiva(vetor, 0, q-1, vetor_de_chaves[i])
    if indice == -1:
        print(f"a chave {vetor_de_chaves[i]} não foi encontrada")
    else:
        print(f"a chave {vetor_de_chaves[i]} foi encontrada no indice {indice}")
    indice = 0