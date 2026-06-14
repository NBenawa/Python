# parent class
class Dog:
    legs = 4
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} says: Bark!!!')

    def getLegs(self):
        print (self.legs)

dog = Dog('Roxy')
dog.getLegs()
dog.speak()

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: vaf vaf vaf!!!')
    pass

chihuahua = Chihuahua('Panter')
chihuahua.getLegs()
chihuahua.speak()