class Car :
    def __init__(self,value1='blue',value2=100):
        self.color = value1
        self.speed = value2
    
    def up_speed(self, value):
        self.speed += value
    
    def down_speed(self, value):
        self.speed -= value

if __name__ == "__main__":
    mycar = Car()
    mycar1 = Car('blue',0)
    mycar2 = Car('red',0)
    print(mycar.color, mycar.speed)
    print(mycar1.color, mycar1.speed)
    print(mycar2.color, mycar2.speed)
    
    mycar.up_speed(10)
    print(mycar.color, mycar.speed)
    print(mycar1.color, mycar1.speed)
    print(mycar2.color, mycar2.speed)
    