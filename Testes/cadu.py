
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


names = ['Cecilia', 'Lisa', 'Marie', 'Jill']
letters = [len(n) for n in names]
names.append('Rosalind')

for name, count in zip(names, letters):
    print('%s has %d letters' % (name, count))

print(names)

