class City(object):

    #initializer method
    def __init__(self,name,celcius):
        #özelliklerin tanımlanacağı fonksiyon
        #attribute
        self.name = name
        self.celcius = celcius

    def getName(self):
        return self.name

    def getTemparature(self):
        return self.celcius

    def  celcius_to_fahrenheit(self):
        "fahrenheit = 38 + 1.8 * celcius -> return fahrenheit"
        fahrenheit = 38 + 1.8 * self.celcius
        return fahrenheit


city = City("Amsterdam",18)
city_name = city.getName()
city_temparature_celcius = city.getTemparature()
city_temparature_fahrenheit = city.celcius_to_fahrenheit()

print("choose celcius(1), fahrenheit(2) for city")
selection = int(input("select 1 or 2\t"))

if selection == 1:
    print("{} temparature:\t".format(city_name),city_temparature_celcius)
elif selection == 2:
    print("{} temparature:\t".format(city_name),city_temparature_fahrenheit)
else:
    print("{} temparature:\t{} celcius, {} fahrenheit".format(city.getName(),city.getTemparature(),city.celcius_to_fahrenheit()))
