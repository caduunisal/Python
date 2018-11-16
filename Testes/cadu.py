
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

############################################################################################################

############################################################################################################
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
############################################################################################################

############################################################################################################


#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#
#    C = (5 * (F-32) / 9). 
        