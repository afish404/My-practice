#4.完成python的传参练习（与上课一致）
file1 = open('myMCserver.txt','r',encoding='utf8')
txt = file1.read()
file1.close()
my_dict = eval(txt)
print(type(my_dict))
print(my_dict)