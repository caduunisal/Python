
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

def my_func (list1, list2):
    #if list1 in list2:
    #    print('OK')
    #else:
    #    print('ERROR')
    #    #print("Simetria: ", x)
    print(list1[2])

list1 = [10, 20, 30]
list2 = [10]

my_func(list1, list2)



#####################################################################################