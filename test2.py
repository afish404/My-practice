#2、练习单例模式，原理与上课一致即可

class VidioPlayer(object):
    top = None
    
    def __new__(cls,*args,**kwarge):
        if cls.top == None:
            cls.top = super().__new__(cls)
        return cls.top
    
    def __init__(self,name):
        self.player = name
    
bilibili = VidioPlayer('B站')
tiktok = VidioPlayer('抖音')
print(bilibili)
print(tiktok)
print(bilibili.player)
print(tiktok.player)
print(bilibili is tiktok)