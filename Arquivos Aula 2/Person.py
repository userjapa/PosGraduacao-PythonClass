class Person:
    first_name = None
    last_name = None
    birth = None

    def __init__(self, first_name = '', last_name = '', birth = ''):
        self.first_name = first_name
        self.last_name  = last_name
        self.birth      = birth

    def greet(self):
        print(f'Hello! My name is {self.first_name} {self.last_name}!')

me = Person()
me.first_name = 'Willian Hiroshi'
me.last_name = 'Simabukuro'
me.birth = '1996-06-13'
print(me)
me.greet()

stranger = Person('Jose', 'Olivia', '1990-10-10')
print(stranger)
stranger.greet()

test = Person(last_name='Test')
print(test)
test.greet()

class Student (Person):
    
