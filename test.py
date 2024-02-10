import random
from tkinter import *
class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.thirst = 50
    def get_home(self):
        self.home = House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        self.job = Job(job_list)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        elif self.home.water <= 0:
            self.shopping("water")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            elif self.thirst >= 100:
                self.thirst = 100
                return
            self.satiety += 5
            self.thirst += 5
            self.home.food -= 5
            self.home.water -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        self.thirst -= 2
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 15:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print("I bought fuel!")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food!")
            self.money -= 50
            self.home.food += 50
        elif manage == 'water':
            print("Bought water!")
            self.money -= 5
            self.home.water += 5
        elif manage == 'delicacies':
            print("I'm happy!")
            self.gladness += 10
            self.money -= 15
            self.satiety += 5
    def chill(self):
        self.gladness += 10
        self.home.mess += 10
        self.money -= 15
    def clean_home(self):
        self.gladness -= 10
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 100


    def days_indexes(self, day):
        d = f"Today is the {day} day of {self.name}'s life"
        print(f"{d:=^50}")

        human_i = f"{self.name}'s indexes"
        print(f"{human_i:=^50}")
        print(f"Money: {self.money}")
        print(f"Gladness: {self.gladness}")
        print(f"Satiety: {self.satiety}")
        print(f"Thirst: {self.thirst}")

        home_i = "Home indexes"
        print(f"{home_i:=^50}")
        print(f"Mess: {self.home.mess}")
        print(f"Food: {self.home.food}")
        print(f"Water: {self.home.water}")

        car_i = f"{self.car.brand} car indexes"
        print(f"{car_i:=^50}")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")

        home_i = "Home indexes"
        print(f"{home_i:=^50}")


        car_i = f"{self.car.brand} car indexes"
        print(f"{car_i:=^50}")
        print(f"Fuel = {self.car.fuel}")
        print(f"Strength = {self.car.strength}")
    def is_alive(self):
        if self.gladness <= 0:
            print("Depression....")
            return False
        elif self.satiety < 0:
            print("Dead....")
            return False
        elif self.money < -100:
            print("Bankrupt...")
            return False
    def live(self, day):
        if self.is_alive() == False: # not False => True
        # if not self.is_alive(): # not False => True
            return False
        if self.home is None:
            print("Settled in the home")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"I have job {self.job.job}, salary {self.job.salary}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 10 or self.thirst < 10:
            print("Go eat or drink!")
            self.eat()

        elif self.gladness < 10:
            if self.home.mess > 15:
                print("Go clean home")
                self.clean_home()
            else:
                print("Time to chill")
                self.chill()
        elif self.money < 0:
            print("Start working!")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car!")
            self.to_repair()
        elif dice == 1:
            print("Time to chill")
            self.chill()
        elif dice == 2:
            print("Start working!")
            self.work()
        elif dice == 3:
            print('Time clean')
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            self.shopping(manage="delicacies")



class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False

class House:
    def __init__(self):
        self.mess = 10
        self.food = 0
        self.water = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

job_list = {"Python developer": {"salary": 40, "gladness_less": 10},
            "C++ developer": {"salary": 60, "gladness_less": 4},
            "Java developer": {"salary": 50, "gladness_less": 8},}

brands_of_car = {"BMW": {"fuel": 100, "strength": 120, "consumption": 14},
                 "Lada": {"fuel": 80, "strength": 40, "consumption": 12},
                 "Ford": {"fuel": 60, "strength": 80, "consumption": 8},
                 "Ferrari": {"fuel": 50, "strength": 90, "consumption": 16}}


h = Human("Oleg")
for day in range(1, 100000):
    if h.live(day) == False:
        break