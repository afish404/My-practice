class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_info(self):
        print(f"my name is {self.name},I'm {self.age} years old")
    
    def grow_up(self):
        self.age += 1
        

zhangsan = Person('张三',21)
zhangsan.grow_up()
zhangsan.age += 1
zhangsan.get_info()