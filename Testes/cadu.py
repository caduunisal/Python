
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

import logging

logging.getLogger().setLevel(logging.WARNING)

def my_function():
    logging.debug('Some debug info')
    logging.error('A real error')
    logging.debug('More debugging')

my_function()



####################################################################################









