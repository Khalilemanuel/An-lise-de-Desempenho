# Questões de programação Atividade 2

# Questão 1:

def media_aritmetica(lista):
    if len(lista) == 0:
        return None
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)

# Teste da função media_aritmetica

print(media_aritmetica([4,8,6,2])) # Deve retornar 5.0

# Questão 2:

def fatorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        #sem for
        return n * fatorial(n - 1)

# Teste da função fatorial

print(fatorial(5)) # Deve retornar 120
print(fatorial(0)) # Deve retornar 1

# Questão 3:

def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

# Teste da função contar_palavras   

print(contar_palavras("Ola mundo cruel")) # Deve retornar 3

# Questão 4:

def soma_elementos_matriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma

# Teste da função soma_elementos_matriz

matriz = [[1, 2], [3, 4]]
print(soma_elementos_matriz(matriz)) # Deve retornar 10

# Questão 5:

def segundo_maior_numero(lista):
    if len(lista) < 2:
        return None
    maior = segundo_maior = float('-inf')
    for numero in lista:
        if numero > maior:
            segundo_maior = maior
            maior = numero
        elif maior > numero > segundo_maior:
            segundo_maior = numero
    return segundo_maior

# Teste da função segundo_maior_numero
print(segundo_maior_numero([3,7,9,5])) # Deve retornar 7

# Questão 8:

def maior_elemento_da_matriz(matriz):
    if not matriz or not matriz[0]:
        return None
    maior = float('-inf')
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    return maior

# Teste da função maior_elemento_da_matriz
matriz = [[3, 7] , [2, 9] , [5, 1] ]
print(maior_elemento_da_matriz(matriz)) # Deve retornar 9

# Questão 9:

def mover_zero_pfinal(lista):
    if not lista:
        return None
    nova_lista = [num for num in lista if num != 0]
    zeros = [0] * (len(lista) - len(nova_lista))
    return nova_lista + zeros

# Teste

print(mover_zero_pfinal([0, 3, 0, 5, 1, 0, 2])) # Deve retornar [3, 5, 1, 2, 0, 0, 0]

# Questão 10:

def potencia_inteira(b,e):
    if e < 0:
        return None
    resultado = 1
    for _ in range(e):
        resultado *= b
    return resultado
# Teste da função potencia_inteira
print(potencia_inteira(2, 10)) # Deve retornar 1024