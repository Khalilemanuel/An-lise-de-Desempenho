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

# Questão 6:

def soma_dos_digitos(n):
    lista = [int(d) for d in str(n)]
    return sum(lista)

# Teste da função soma_dos_digitos

print(soma_dos_digitos(1234)) # Deve retornar 10

# Questão 7:

def verificar_anagrama(s1, s2):
    return sorted(s1) == sorted(s2)

# Teste da função verificar_anagrama

print(verificar_anagrama("roma","amor"))
print(verificar_anagrama("casa","sala"))
