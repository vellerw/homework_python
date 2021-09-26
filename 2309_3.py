class Car:
    type = 'Car'

    def __init__(self, speed):
        self.speed = speed

class Mitsubishi(Car):
    model = 'Mitsubishi'

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed

class Porsche(Car):
    model = 'Porsche'

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed

class Ferrari(Car):
    model = 'Ferrari'

    def __init__(self, speed):
        super().__init__(speed)
        self.speed = speed

pos_l = 0
pos_p = 0
pos_m = 0
finish_race = 1000
l = Ferrari(270)
p = Porsche(280)
m = Mitsubishi(255)
while pos_m < finish_race and pos_p < finish_race:
    pos_m += m.speed
    pos_p += p.speed
if pos_p > pos_m:
    print('Porsche')
if pos_m > pos_p:
    print('Mitsubishi') 
