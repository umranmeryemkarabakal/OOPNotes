#super class
class Animal(object):

    def __init__(self,name,age):
        #encapsulation
        self.name = name #global variable
        self.__age = age #private variable

    #get and set methods
    #global method
    def getAge(self):
        print("Animal age:\t",self.__age)
        return self.__age
    
    def setAge(self,newAge):
        self.__age = newAge
        return self.__age

    #private method
    def __increase(self):
        self.__age += 1
        return self.__age
    
    def getName(self):
        print("Animal name:\t",self.name)

animal1 = Animal("monkey",3)

animal1.__age = 2
print("get age method:\t",animal1.getAge())

animal1.setAge(2)
print("after set method:\t",animal1.getAge())

"""animal1.__increase()
print("after raise:\t",animal1.getAge())"""

#inheritence
#sub class
class Dog(Animal):

    def __init__(self,name,age,color):
        super().__init__(name,age) #Animal class'ının initializer methodu'ndaki attribute'lerin kullanılmasını sağlar
        self.color = color
        print("dog is created")

    #overriding
    def getName(self):
        print("Dog name:\t",self.name)

dog1 = Dog("oliver",3,"black")

dog1.getName()
#monkey calls overriding method
dog1.getAge() #kendi clasındakini çalıştırır

#polymorphism
class Bird(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
        print("Bird created")

        def getName(self):
            print("Bird name:\t",self.name)

bird1 = Bird("bead",1)
bird1.getName()