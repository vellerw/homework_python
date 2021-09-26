import keyword
import random


class Person():
    def __init__(self, name):
        self.name = name

    def talk(self, text):
        print(self.name, ': ', text)

p = Person('Sem')
p2 = Person('Fin')

speak_list = ['Hello', 'How are you?' , 'How are you doing?', 'Thank you so much', 'Fine', 'Good', 'I’m ok' , 'How about you?' , 'And you?', 'See ya later', 'Don’t mention it', 'I think', 'How’s your family?']

n = 0
while n < 5:
    p.talk(random.choice(speak_list))
    p2.talk(random.choice(speak_list))
    n += 1 
