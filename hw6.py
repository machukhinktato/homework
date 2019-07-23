class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False
        # if self._is_police == True:
        #     print('И спортивная тоже, милицейская!')
        # else:
        #     print('А вот спортивная чёт не милицейская')

    def go(self):
        print('Машина {} начала свое движение!'.format(self.name))

    def stop (self):
        print('Машина {} остановилась!'.format(self.name))

    def turn (self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class TownCar(Car):
    def __init__ (self, speed, color, name):
        Car.__init__(self,speed,color,name)
        self.is_police =  False


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police =  False


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name)
        self.is_police = False

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        Car.__init__(self, speed, color, name)
        self.is_police = is_police


my_car = Car(250,'Blue','Subaru Impreza')
town_car = TownCar (180, 'Red','Smart')
work_car = WorkCar(220,'Silver','Toyota Camry')
sport_car = SportCar(350, 'Yellow', 'Porsche 911')
police_car = PoliceCar(150, 'Grey', 'UAZ')


my_car.go()
my_car.turn('на 180 градусов')
my_car.stop()
my_car.is_police
print('Эта малышка цвета: ', my_car.color)

if police_car.is_police == True:
    print('Уазик то, действительно милицейский!')

if sport_car.is_police == True:
    print('И спортивная тоже, милицейская!')
else:
    print('А вот спортивная чёт не милицейская')

