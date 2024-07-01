from abc import ABC, abstractclassmethod

class Animal(ABC):

    @abstractclassmethod
    def walk(self):
        pass

    def run(self):
        pass

class Bird(Animal):
    def __init__(self):
        print("bird")

    def walk(self):
        print("walk")

#animal = Animal()
bead = Bird()

#abstract şartları:
#Animal classıyla obje oluşturulamaz
#Animal classında abstractmethod olarak tanımlanan methodlar Bird classında da kullanmak zorunludur