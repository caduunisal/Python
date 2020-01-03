
#vrvl=0
#
#if vrvl == 0: 
#    print("Hello World!")
#else:
#    print("Welcome Back!")


#words = ['cat', 'dog', 'rabbit']
#
#for animal in words:
#    print(animal, len(animal))


#for i in range(100):
#    if (i%2) == 0:
#        print(i)

#while True:
#    reply = input('Enter Text:')
#    if reply == 'stop': break
#    print(reply.upper())


#print(range(10))
#list(range(10))

#from kivy.app import App
#from kivy.uix.button import Button
#
#class TestApp(App):
#    def build(self):
#        return Button(text='Hello World')
#
#TestApp().run()

###################################################
# Item 4 Use ZIP to process iterators in parallel #
###################################################
#names = ['Cecilia', 'Lisa', 'Marie', 'Jill']
#letters = [len(n) for n in names]
#names.append('Rosalind')
#
#for name, count in zip(names, letters):
#    print('%s has %d letters' % (name, count))
#
#print(names)
#
#--------------------------------------------------

#names = ['Cecilia', 'Lisa', 'Marie', 'Jill']
#letters = [len(n) for n in names]
#names.append('Rosalind')
#
#from itertools import zip_longest
#for name, count in zip_longest(names, letters):
#    if count is None:
#        print('%s is of unknow lenght' % name)
#    else:
#        print('% has %d letters' % (name, count))
#
#print(names)
###################################################


##################################################################
# Item 6 Take advantage of each block in TRY/EXCEPT/ELSE/FINALLY #
##################################################################
#fd = open('file.txt')
#try:
#    data = fd.read()
#finally:
#    fd.close()
#
#print(data)


#fd = open('file.txt')
#fd1 = open('file1.txt', 'w')
#try:
#    data = fd.read()
#    fd1.write(data)
#finally:
#    fd.close()
#    fd1.close()
#
#print(data)
##################################################################



####################################################################################
# Item 7 Consider CONTEXTLIB and with statements for reusable TRY/FINALLY behavior #
####################################################################################
#
#import logging
#
#logging.getLogger().setLevel(logging.WARNING)
#
#def my_function():
#    logging.debug('Some debug info')
#    logging.error('A real error')
#    logging.debug('More debugging!')
#
#my_function()

####################################################################################


############################################################
# Item 8 Use list comprehensions instead of MAP and FILTER #
############################################################
#
#a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#square = [x**2 for x in a]
#print(square)
#
############################################################


#lst = [1, 'Python', 'List', 20]
#for item in lst:
#    print(item)

######################################################################################
# https://powerpython.wordpress.com/2012/04/09/aula-python-estrutura-de-repeticao-1/ #
######################################################################################

#####################################################################################
# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o  #
# valor seja inválido e continue pedindo até que o usuário informe um valor válido. #
#####################################################################################
#
#number = int(input('Entre com um valor entre 0 e 10: '))
#
#while 0 > number or 10 < number:
#    number = int(input('Entre com um numero valido: '))

#####################################################################################







################################################################################
# http://www-di.inf.puc-rio.br/~milidiu/inf1025/exercicios/Lista12_INF1025.pdf #
################################################################################


#####################################################################################
# 1. Crie uma função que recebe uma lista de números e
#    a. retorne o maior elemento
#    b. retorne a soma dos elementos
#    c. retorne o número de ocorrências do primeiro elemento da lista
#    d. retorne a média dos elementos
#    e. retorne o valor mais próximo da média dos elementos
#    f. retorne a soma dos elementos com valor negativo
#    g. retorne a quantidade de vizinhos iguais

#def my_func (list):
#    print('a. Maior elemento: ', max(lst))
#    #-------------------------------------------------------
#    print('b. Soma: ', sum(lst))
#    #-------------------------------------------------------
#    print('c. No. Ocorrencias: ', list.count(list[0]))
#    #-------------------------------------------------------
#    print('d. Media: ', sum(list)/len(list))
#    #-------------------------------------------------------
#    avg = sum(list) / len(list)
#    diffs = {value: abs(value - avg) for value in lst}
#    print('e. Mais proximo: ', min(diffs, key=diffs.get))
#    #-------------------------------------------------------
#    sumnegval = 0
#    for negval in list:
#        if negval < 0:
#            sumnegval = sumnegval + negval
#    print('f. Valores Negativos: ', sumnegval)
#    #-------------------------------------------------------
#    oldval = 1000
#    rep = 0
#    for val in list:
#        if val == oldval:
#            #print(val)
#            rep = rep + 1
#        else:
#            oldval = val
#            
#
#    print('g. Vizinhos: ', rep) 
#
#lst = [10, 50, -25, 200, 200, 10, 67.3, 67.3, 10, -5, -5, 10]
#my_func(lst)

#####################################################################################




#####################################################################################
# a) Faça uma função que receba duas listas e retorne True se são iguais 
#     ou False caso contrário.
# 
# PS: Duas listas são iguais se possuem os mesmos valores e na mesma ordem.
#
# b) Faça uma função que receba duas listas e retorne True se têm os mesmos elementos 
#    ou False caso contrário 

# a)
#def my_func (list1, list2):
#
#    rc = 0
#    if len(list1) != len(list2):
#        print('Different lists!')
#        rc = 1
#    else:
#        i = 0
#        while i < len(list1):
#            if list1[i] == list2[i]:
#                i = i+1
#            else:
#                print('Different lists!')
#                rc = 1
#                break
#            
#    if rc == 0:
#        print('Equal lists!')
#
#list1 = [15, 20, 30]
#list2 = [15, 20, 30]
#
#my_func(list1, list2)


# b)
#def my_func (list1, list2):
#
#    rc = 0
#    if len(list1) != len(list2):
#        print('False')
#        rc = 1
#    else:
#        i = 0
#        while i < len(list1):
#            if list1[i] == list2[i]:
#                i = i+1
#            else:
#                print('False')
#                rc = 1
#                break
#            
#    if rc == 0:
#        print('True')
#
#list1 = [15, 20, 30]
#list2 = [15, 20, 30]
#
#my_func(list1, list2)

#####################################################################################


##########################################################################################################
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, #
# between 2000 and 3200 (both included).                                                                 #
# The numbers obtained should be printed in a comma-separated sequence on a single line.                 #
##########################################################################################################

#list1 = []
#for num in range(2000, 3201):
#    if (num%7) == 0 and (num%5) == 1:
#        list1.append(num)
#        #print('Divisible by 7 and NOT multiple of 5: ', num)
#print(list1)

##########################################################################################################




############################################################################################################
# Write a program that accepts sequence of lines as input and prints the lines after making all characters #
# in the sentence capitalized.                                                                             #
############################################################################################################
#
#lines = []
#while True:
#    s = input()
#    if s:
#        lines.append(s.upper())
#    else:
#        break;
#
#for sentence in lines:
#    print (sentence)
#
############################################################################################################


############################################################################################################
# Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 30 posições. Crie uma     #
# função que recebe o vetor preenchido e substitua todas as ocorrência de valores positivos por 1 e todos  #
# os valores negativos por 0.                                                                              #
############################################################################################################
#
#list = []
#i = 1
#
#def insert_array (digit):
#    if int(digit)>=0:
#        list.append('1')
#    else:
#        list.append('0')
#
#while i<11:
#    digit = input('Valor: ')
#    insert_array(digit)
#    i = i+1
#
#
#print(list)
#
############################################################################################################



############################################################################################################
# Crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + … + n/m, para um valor de n    # 
# definido pelo usuário. Verifique se o valor de n definido pelo usuário é positivo e, caso não seja,      #
# solicite outro valor até ser fornecido um valor positivo.                                                #
############################################################################################################



############################################################################################################










############################################################################################################
# Tendo uma matriz 10×10 preenchida com valores aleatórios entre 10 e 50, mostre qual é o maior valor      # 
# existente na matriz desconsiderando os elementos da diagonal principal.                                  #
############################################################################################################
#
#mtrz = []
#n = 10
#
#for i in range(n):
#    mtrz.append(i)
#    for j in range(n):
#        mtrz.append(j)
#        #print(i, j)
#print(mtrz)
#
############################################################################################################


#matriz = []
#n = 2
#for i in range(n):
#   tmp = []
#   for j in range(n):
#       elemento = input("Digite o elemento da posicao {0}-{1} ".format(i,j))
#       tmp.append(elemento)
#
#   matriz.append(tmp[:])
#print(matriz)


# https://wiki.python.org.br/ListaDeExercicios




############################################################################################################
# Faça um Programa que mostre a mensagem "Alo mundo" na tela.                                              #
############################################################################################################

############################################################################################################
#print('Alo mundo')

############################################################################################################
# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].           #
############################################################################################################
#num = input('Digite um numero: ')
#print('O numero informado foi: ', num)

############################################################################################################

############################################################################################################
# Faça um Programa que peça dois números e imprima a soma.                                                 #
############################################################################################################
#num1 = input('Primeiro numero: ')
#num2 = input('Segundo numero: ')
#print('Soma: ', int(num1) + int(num2))
#
############################################################################################################


############################################################################################################
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
############################################################################################################
#notas = []
#i = 4
#
#while i > 0:
#        notas.append(int(input("Bimestre: ")))
#        i = i-1
#
#media = sum(notas) / len(notas)
#print("Media: ", media)
#
############################################################################################################


############################################################################################################
# Faça um Programa que converta metros para centímetros.
############################################################################################################
# 1 metro = 100 centimetros
#dado = float(input("Medida em metros: "))
#print("Medida em centimetros: ", (dado*100))
#
############################################################################################################



############################################################################################################
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
############################################################################################################
#pi = 3.14
#raio = float(input("Entre com o raio: "))
#area = (pi * (raio ** 2))
#
#print("Area: ", area)
#
############################################################################################################


############################################################################################################
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
############################################################################################################
#dado = float(input("Entre com o lado do quadrado: "))
#area = (dado * dado)
#print("Dobro da area: ", (area * 2))
#
############################################################################################################


############################################################################################################
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
# e mostre o total do seu salário no referido mês.
############################################################################################################
#valor_hora = float(input("Valor hora: "))
#horas_mes = float(input("Horas trabalhadas no mes: "))
#
#print("Salario Mensal: ", (valor_hora * horas_mes))
#
############################################################################################################


############################################################################################################
# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus 
# Celsius.
#
# C = (5 * (F-32) / 9). 
############################################################################################################
#temp = float(input("Temperatura em Farenheit: "))
#print("Temperatura Celsius: ", (5 * (temp-32) / 9))
#
############################################################################################################





'''
lista = [1, 2.5, 'DevCode', [5,6] ,4, 4]

print (lista[0])
print (lista[1])
print (lista[2])
print (lista[3])
print (lista[3][0])
print (lista[3][1])
print (lista[1:3])
print (lista[1:6])
print (lista[1:6:2])

lista.append('IBM')

for elemento in lista:
        print(elemento)
   
print(lista.index('IBM'))
print(lista.count(4))
lista.reverse()
print(lista)
lista.extend([10, 20])
print(lista)
'''






'''
def calc (opt):
        if opt == "adi":
                print("Soma")
        elif opt == "sub":
                print("Subtracao")
        elif opt == "div":
                print("Divisao")
        elif opt == "mul":
                print("Multiplicacao")
        else:
                print("Funcao invalida")

calc("mul")
'''





'''
list = [10,15,20,25,30]

for item in list:
        if item > 20:
                print(item)
        else:
                print("NULL")
'''


# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 

'''
peso_peixes = input ("Digite o peso: ")
print("Peso pescado: ", peso_peixes, "Kg")
excedente = int(peso_peixes) - 50
if excedente > 0:
    print("Excedente: ", excedente, "Kg")
    multa = excedente * 4
    print("Multa: R$", multa)
else:
    print("Peso em conformidade!")
'''


# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez. 
'''
list = []
i = 2

while i > 0:
    nota = float(input("Nota: "))
    list.append(nota)
    i = i-1

media = float(list[0] + list[1]) / 2

if media >= 7 and media != 10:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com Distincao")
'''

#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor
#  serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina. 


# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 
'''
list = []
i = 5
pos = 0
neg = 0

info = input("Telefonou para a vitima? [y|n]")
list.append(info)
info = input("Esteve no local do crime? [y|n]")
list.append(info)
info = input("Mora perto da vitima? [y|n]")
list.append(info)
info = input("Devia para a vitima? [y|n]")
list.append(info)
info = input("Ja trabalhou para a vitima? [y|n]")
list.append(info)

for value in list:
    if value == 'y':
        pos = pos+1
    else:
        neg = neg+1
print("Pos: ", pos)
print("Neg: ", neg)

if pos == 2:
    print("Suspeito")
elif pos == 3 or pos == 4:
    print("Cumplice")
elif pos == 5:
    print("Assassino")
else:
    print("Inocente")
'''



'''
# Dicionarios
dict = {}
dict['a'] = 'Carlos'
dict['b'] = 'Eduardo'
dict['c'] = 'Ramos'

print (dict['b'])
print (dict)
'''


'''
# Fatorial
def fat(n):
  if n <= 1:
    return 1
  return fat(n-1) * n

print(fat(6))
'''


# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
#
#true = 1
#
#while true:
#    number = int(input("Insira uma nota [0-10]:"))
#    if number <0 or number > 10:
#        print("Nota invalida!")
#    else:
#        print("Nota OK!")
#        break


# http://www.galirows.com.br/meublog/programacao/exercicios-resolvidos-python/

# Exercício 1: faça um algoritmo que solicite ao usuário números e os armazene em 
# um vetor de 10 posições. Crie uma função que recebe o vetor preenchido e substitua 
# todas as ocorrência de valores positivos por 1 e todos os valores negativos por 0.

#def troca(vet):
#    for i in range(10):
#        if vet[i] >= 0:
#            vet[i] = 1
#        else:
#            vet[i] = 0
#    return vet
# 
#vet = [0]*10
#for i in range(10):
#    vet[i] = int(input('Digite um valor: '))
#print (vet)
#troca(vet)
#print (vet)

# Exercício 3: Faça um algoritmo que solicite ao usuário números e os armazene em um 
# vetor de 20 posições. Crie uma função que recebe o vetor preenchido e substitua todas 
# as ocorrências de valores negativos por zero, as ocorrências de valores menores do que 
# 10 por 1 e as demais ocorrências por 2.

#def troca(vet):
#    for i in range(10):
#        if vet[i] < 0:
#            vet[i] = 0
#        elif vet[i] < 10:
#            vet[i] = 1
#        else:
#            vet[i] = 2
#    return vet
#
#vet = [0]*10
#for i in range(10):
#    vet[i] = int(input('Digite um valor: '))
#
#troca(vet)
#print(vet)

# Exercício 4: crie um algoritmo que solicite 3 valores que representarão os lados de um triângulo. 
# Considere que não importa a ordem que serão fornecidos os valores, podendo ser fornecido primeiro 
# a hipotenusa e depois os catetos, ou primeiro os catetos e depois a hipotenusa, etc. Crie também 
# uma função que recebe o vetor e retorna se os lados informados formam um triângulo retângulo. 
'''
def confere(vet):
    if ((vet[0] + vet[1]) < vet[2]) or ((vet[1] + vet[2]) < vet[0]) or ((vet[2] + vet[0]) < vet[1]):
        return "Nao forma triangulo"
    elif vet[0] == vet[1] and vet[1] == vet[2]:
        return "Triangulo Retangulo"
    elif vet[0] != vet[1] and vet[1] != vet[2]:
        return "Triangulo Escaleno"
    else:
        return "Triangulo Isosceles"

vet = [0]*3
for i in range(3):
    vet[i] = int(input('Digite um valor: '))

print(confere(vet))
'''
'''
str = "Python Training"

print (str.replace("Python", "PYTHON"))
print ("-" * 20)
print (10 // 3)
print (str.lower())
print (str[1:-2])
'''


'''
nome = "Carlos"
sobrenome = "Ramos"

print (f"Nome completo: {nome} {sobrenome}")
'''

'''
elegible = False

if elegible:
    print ("Elegible for loan")
else:
    print ("Not elegible for loan")

'''

'''
name = input ("Input your complete Name: ")

if len(name) > 50:
    print ("Characters exceeded... Should be less than 50")
elif len(name) < 3:
    print ("Less than 3 characters... Try again")
else:
    print ("Name looks good!")

'''

'''
started = False

while True:
    digit = input ("> ").upper()
    if (digit == "HELP"):
        print ("""
            Start => Satrt the car
            Stop  => Stop the car
            Quit  => Exit the program 
        """) 
        continue
    if digit == "START":
        if started:
            print ("Car already started!")
            #started = True
        else:
            print ("Car started...")
            started = True
    elif digit == "STOP":
        if not started:
            print (" Car already stopped!")
            #started = False
        else:
            print ("Car stopped...")
            started = False
    elif (digit == "QUIT"):
        print ("Bye bye!")
        break
    else:
        print ("Sorry, I dont't understand that. Type 'help' to more info!")

'''

'''
prices = [10, 20, 30]
total = 0

for item in prices:
    total += item

print (f"Total: {total}")
'''

'''
for x in range(4):
    for y in range(3):
        print (f"({x}, {y})")
'''

'''
numbers = [5, 2, 5, 2, 10]

for x in numbers:
    print("x" * x)

'''

'''
lst = [200, 100, 30, 70, 25]
max = lst[0]

for number in lst:
    if number > max:
        max = number

print (max)
'''

'''
matrix = [
         [0, 1, 2],
         [10, 20, 30],
         [100, 200, 300],
         [1000, 2000, 3000, 4000]
         ]
matrix[2][2] = 500
print (matrix[2][2])
matrix.append(1234)
print(matrix)

'''
'''
lst = [10, 20, 30, 40, 50]
lst.insert(1, 15)
print(lst)
lst.remove(30)
print(lst)
#lst.clear()
#print(lst)
lst.append(3)
print(lst)
lst.sort()
print(lst)
'''

'''
# Removendo itens duplicados em uma lista

lst = [10, 20, 20, 30, 20, 10, 15]
unique = []

for item in lst:
    if (item in unique):
        continue
    else:
        unique.append(item)
unique.sort()
print(unique)

'''

'''
# Tuples: Diferentemente das listas, nao podem ser modificadas

coordinates = (10, 20, 30)
x, y, z = coordinates
print(f"x = {x} | y = {y} | z = {z}")

'''


# Dictonaries
'''
customer = {
    "name": "Carlos Eduardo Ramos",
    "address": "Rua Ari Meireles 594",
    "age": 41,
    "email": "kadu.unisal1@gmail.com",
    "verified": True
}

print(customer["name"])
'''

'''
numbers = {
    "1": "Um",
    "2": "Dois",
    "3": "Tres",
    "4": "Quatro",
    "5": "Cinco"
}

phone = input("Type a number: ")
output = ""

for ch in phone:
    output += numbers.get(ch, "!") + " "

print(output)

'''

'''
def greet_user(name):
    print(f"Hello, {name}!")

name = input("Type you name: ")
greet_user(name.upper())

'''

'''
lst = [10, 20, 30]
lst[1] = 15
lst.append(40)
print(lst)
lst.pop(2)
print(lst)

lst.reverse()
print(lst)
'''

'''
# Removendo vogais
vogais = ["a", "e", "i", "o", "u"]
out_name = []
loop = True

while loop:
    vog = 0
    con = 0
    name = input("Nome '[EXIT|SAIR] to quit': ")
    if (name.lower() == "sair" or name.lower() == "exit"):
        print("BYE BYE!")
        break

    for item in name.lower():
        if item in vogais:
            vog += 1
            continue
        if item != " ":
            out_name.append(item)
            con += 1

    print(out_name)
    print(f"Vogais: {vog} | Consoantes: {con}")
    out_name = []

'''

'''
# Arquivos
fd = open("file.txt", "w")
for item in range(5):
    fd.write(f"{item}")
fd.close()

fd = open("file.txt", "r")

for item in fd.read():
    if (int(item) % 2) == 0:
        print(f"{item}")
fd.close()

'''



'''
# Arquivos
fd = open("file.txt", "w")
for item in range(10):
    fd.write(f"{item}")
fd.close()

fd = open("file.txt", "r")

for item in fd.read():
    if (int(item) % 2) == 0:
        print(f"{item}")
fd.close()
'''

'''
# Treinando tartarugas
import turtle            # permite usar as funções e objetos do módulo turtle
wn = turtle.Screen()     # cria uma janela gráfica
wn.bgcolor("lightblue")
cadu = turtle.Turtle()   # cria um turtle chamado cadu
cadu.forward(150)        # manda o cadu se mover 150 unidades para frente
cadu.left(90)            # roda de 90 graus para a esquerda
cadu.forward(75)         # desenha o segundo lado do retângulo
cadu.left(90)
cadu.forward(150)
cadu.left(90)
cadu.color("red")
cadu.forward(75)
wn.exitonclick()
'''


# Treinando Tartarugas
import turtle

def desenhaQuadrado (t, tam):
    '''Faca a tartaruga t desenhar um quadrado de lado tam'''

    for i in range(4):
        t.color("red")
        t.forward(tam)
        t.left(90)
        #t.circle(15)

def desenhaCirculo (t, raio):
    '''Faca a tartaruga t desenhar um circulo de raio raio'''

    t.circle(raio)

wn = turtle.Screen()
wn.bgcolor("lightblue")

cadu = turtle.Turtle()
desenhaQuadrado(cadu, 100)

carlos = turtle.Turtle()
carlos.penup()              # Ajustando posicao de novo desenho
carlos.goto(200,200)        # Ajustando posicao de novo desenho
carlos.pendown()            # Ajustando posicao de novo desenho
desenhaCirculo(carlos, 50)
wn.exitonclick()






