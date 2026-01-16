class Bank:
    def __init__(self,money):
        self.__money = money
        
    def HowMany(self):
        return self.__money
    
    def SaveMoney(self,amount):
        if amount > 0:
            self.__money += amount
            print('sucess')
        else:
            print('Invalid')
    
    def TakeMoney(self,amount):
        if 0 < amount < self.__money:
            self.__money -= amount
            print('sucess')
        else:
            print("Invalid")

if __name__ == '__main__':
    Acount = Bank(100)
    print(Acount.HowMany())
    Acount.SaveMoney(50)
    print(Acount.HowMany())
    Acount.TakeMoney(30)