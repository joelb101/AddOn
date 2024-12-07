<<<<<<< HEAD


class Car:

    def __init__(self,name,price):    #constructor
        self.name=name
        self.price=price


    def print_car_details(self):    #all methods in class need self as first argument
        print(self.name,self.price)


class Nano(Car): #inheritance
    def print_car_details(self): #method overrriding
        #print("nano")
        return super().print_car_details() # calling parent class from child class

c1=Car("Toyota Corolla",10000)
c2=Car("Jeep Wrangler",20000)
c3=Car("Volkswagon polo",30000)

n1=Nano("NAno",2000)          

n1.print_car_details()


c1.print_car_details()     
c2.print_car_details()
c3.print_car_details()

=======


class Car:

    def __init__(self,name,price):    #constructor
        self.name=name
        self.price=price


    def print_car_details(self):    #all methods in class need self as first argument
        print(self.name,self.price)


class Nano(Car): #inheritance
    def print_car_details(self): #method overrriding
        #print("nano")
        return super().print_car_details() # calling parent class from child class

c1=Car("Toyota Corolla",10000)
c2=Car("Jeep Wrangler",20000)
c3=Car("Volkswagon polo",30000)

n1=Nano("NAno",2000)          

n1.print_car_details()


c1.print_car_details()     
c2.print_car_details()
c3.print_car_details()

>>>>>>> master
#Car.print_car_details(c1) => alternate method for calling function without self