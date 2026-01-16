class Girl:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    def __HowOld(self):
        return self.__age
    
    def BoyFriend(self):
        return self.__HowOld()
    
LiLi = Girl("莉莉",18)
print(LiLi.BoyFriend())