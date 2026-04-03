# Questões de programação para a Mini Maratona

# Questão 1:

def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Teste da função soma_lista:

print(soma_lista([1,2,3,4])) # Deve retornar 10

# Questão 2:

def numeros_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return len(pares)

# Teste da função numeros_pares

print(numeros_pares([1,2,3,4,5,6])) # Resultado esperado: 3

# Questão 3:

def maior_numero(lista):
    if len(lista) == 0:
        return None
    maior = lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

# Teste da função maior_numero

print(maior_numero([3,7,2,9,5])) # saida esperada: 9

# Questão 4:

def contar_maiores_que_x(lista, x):
    contador = 0
    for numero in lista:
        if numero > x:
            contador += 1
    return contador

# Teste da função contar_maiores_que_x

print(contar_maiores_que_x([1,2,3,4,5], 3)) # saida esperada: 2

# Questão 5:

def soma_dos_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return sum(pares)

# Teste da função soma_dos_pares

print(soma_dos_pares([1,2,3,4,5,6])) # saida esperada: 12

# Questão 6:

def ver_elemento(lista, x):
    for numero in lista:
        if numero == x:
            return "verdadeiro"
    return "falso"

# Teste da função ver_elemento 

print(ver_elemento([4,7,1,9], 7)) # saida esperada: True

# Questão 7:

def inverter_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

# Teste da função inverter_lista

print(inverter_lista([1,2,3,4])) # saida esperada: [4,3,2,1]

# Questão 8:

def contar_ocorrencias(lista, x):
    contador = 0
    for numero in lista:
        if numero == x:
            contador += 1
    return contador

# Teste da função contar_ocorrencias

print(contar_ocorrencias([1,2,2,3,2,4], 2)) # saida esperada: 3

# Questão 9:

def soma_dos_positivos(lista):
    positivos = []
    for numero in lista:
        if numero > 0:
            positivos.append(numero)
    return sum(positivos)

# Teste da função soma_dos_positivos

print(soma_dos_positivos([-1,2,-3,4,5])) # saida esperada: 11

# QUestão 10:

def produto_elemento(lista):
    produto = 1
    for numero in lista:
        produto *= numero
    return produto

# Teste da função produto_elemento

print(produto_elemento([1,2,3,4])) # saida esperada: 24

# Questão 11:

def contar_vogais(s):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in s:
        if letra in vogais:
            contador += 1
    return contador

# Teste da função contar_vogais

print(contar_vogais("Programaçao")) #saida esperada: 5

# Questão 12:

def contar_caracteres(s):
    contador = 0
    for caracter in s:
        contador +=1
    return contador

# Teste da função contar_caracteres

print(contar_caracteres("teste")) # saida esperada: 5

# Questão 13:

def ver_palindromo(s):
    s = s.replace(" ", "").lower() # Remove espaços e converte para minúsculas
    return s == s[::-1]

# Teste da função ver_palindromo

print(ver_palindromo("arara")) # saida esperada: True
print(ver_palindromo("casa")) # saida esperada: False

# Questão 14:

def ocorrencia_de_letra(s, letra):
    contador = 0
    for caracter in s:
        if caracter == letra:
            contador += 1
    return contador

# Teste da função ocorrencia_de_letra

print(ocorrencia_de_letra("banana", "a")) # saida esperada: 3

# Questão 15:

def substituir_caracter(s, antigo, novo):
    resultado = ""
    for caracter in s:
        if caracter == antigo:
            resultado += novo
        else:
            resultado += caracter
    return resultado

# Teste da função substituir_caracter

print(substituir_caracter("banana", "a", "o")) # saida esperada: "bonono"

# Questão 16:

def contar_maiusculas_e_minusculas(s):  
    maiusculas = 0
    minusculas = 0
    for caracter in s:
        if 'A' <= caracter <= 'Z':
            maiusculas += 1
        elif 'a' <= caracter <= 'z':
            minusculas += 1
    return f"maiusculas: {maiusculas}, minusculas: {minusculas}"

# Teste da função contar_maiusculas_e_minusculas

print(contar_maiusculas_e_minusculas("AbCde")) # saida esperada: (2, 5)

# Questão 17:

def remover_espacos(s):
    resultado = ""
    for caracter in s:
        if caracter != " ":
            resultado += caracter
    return resultado

# Teste da função remover_espacos

print(remover_espacos("Olá Mundo")) # saida esperada: "OláMundo"

#questão 18:

def primeiro_caracter(s):
    if len(s) == 0:
        return None
    return s[0]

# Teste da função primeiro_caracter 

print(primeiro_caracter("python")) # saida esperada: "p"