"""
1、在函数内改变函数外某个列表中第一个元素的值（和上课代码原理保持一致即可）
2、练习位置参数，keyword参数，同时练习当你传递位置参数，keyword不正确的时候，出现报错信息，理解报错原因。正确代码可以提交，错误代码也可以提交，在错误代码后面贴上报错记录，或者说这是不对的均可。（和上课代码原理保持一致即可）
3、多值参数练习，元组，字典的传参拆包练习（和上课代码原理保持一致即可）
4.设计一个类，实例化1个对象，会实现下面两种行为

需求
•一只 黄颜色 的 狗狗 叫 小黄
•具有  汪汪叫 行为
•具有  摇尾巴 行为
"""

def changelist(list1):
    list1[0] = 10

list1 = [1,2,3]
print(list1,id(list1))
changelist(list1)
print(list1,id(list1))

def test2(a,*args,**kwargs):
    b = a + 1
    list2 = args
    aaa,bbb = kwargs
    print(b,list2,aaa,bbb)

test2(1 , 1 , 2 , 3 , key1=32 , key2=34 )

def test3(my_tuple,my_dic):
    a,b = my_tuple
    print(a,b)
    c,d = my_dic
    print(c,d) 

test3((1,5),{'love':1314,'like':666})

class Dog:
    
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def spark(self):
        print('汪汪')
        
    def __str__(self):
        return f'名字：{self.name}  颜色：{self.color}'

xiaohuang = Dog('小黄','yellow')
print(xiaohuang.name)
print(xiaohuang.color)
xiaohuang.spark()
print(xiaohuang)