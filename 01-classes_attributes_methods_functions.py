class Quadrilaterals(object):
    #atttributes
    short_side = 3 #meter
    long_side = 7 #meter

    #methods
    def area(self):
        #self objeye ait değişkenleri kullanmak için yazılır
        self.area = self.short_side * self.long_side
        print("area:\t",self.area)

    def perimeter(self):
        self.perimeter = (self.short_side + self.long_side) *2 
        print("perimeter:\t",self.perimeter)
        return self.perimeter

square = Quadrilaterals()
square.short_side = 5
square.long_side = 5
print("long side of square:\t",square.long_side)
print("area of square:\t",square.area())

quadrilateral = Quadrilaterals()
print("method defined",quadrilateral.area)
print("area of quadrilateral:\t",quadrilateral.area())

print("perimeter of square:\t",square.perimeter())
print("perimeter of quadrilateral:\t",quadrilateral.perimeter())


#functions
def calculateArea(short_side,long_side): #parameters
    area = short_side * long_side
    print("area:\t",area)
    return area

result = calculateArea(10,12)

#variables
short_side = 7 
long_side = 8
result1 = calculateArea(short_side,long_side)

print("results:\t",result + result1)



#attribute: özellikler
#behaviour: davranışlar
    