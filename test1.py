#1、练习正则表达式的search，findall，sub，split，用上课的例子练习即可
import re

text = "我的手机号：13812345678，备用号 13987654321"

def use_search():
    pattern = r"1[34578]\d{9}" 
    result = re.search(pattern,text)
    if result:
        print(f'my main number is {result.group()}')
        print(f'it\'s in {result.span()}')

def use_findall():
    pattern = r"1[34578]\d{9}" 
    result = re.findall(pattern,text)
    if result:
        print(result)
        
def use_sub():
    pattern = r"1[34578]\d{9}" 
    result = re.sub(pattern,'*** **** ****',text,count=2)
    print(result)

def use_split(): 
    pattern = r"[ ，：]"
    result = re.split(pattern,text)
    print(result)

use_search()
use_findall()
use_sub()
use_split()