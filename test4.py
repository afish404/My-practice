#3、练习单继承案例，包括super的使用练习（和上课原理保持一致即可）

class Animal:
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f'{self.name} is eatting')
    
class Dog(Animal):
    def spark(self):
        print("汪汪")
    
    def eat(self):
        print(f'{self.name} is eatting well')

WangCai = Dog('旺财')
WangCai.spark()
WangCai.eat()