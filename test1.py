class Students:
    count = 0
    
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        Students.count += 1
    
    @classmethod
    def in_total(cls):
        print(f'the account of animals is{cls.count}')
    
    @staticmethod
    def more_point(num):
        num += 10
        return num
        
zhangsan = Students('张三',21,80)
lisi = Students('李四',19,70)
print(Students.count)
Students.in_total()
print(Students.more_point(75))