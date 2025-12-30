"""
完成列表、字典的增删查改（代码与上课保持一致）
完成字符串的切片
num_str = "0123456789"
截取从 2 ~ 5 位置 的字符串
截取从 2 ~ 末尾的字符串
截取从 开始~ 5 位置 的字符串
截取完整的字符串
从开始位置，每隔一个字符截取字符串
从索引 1 开始，每隔一个取一个
截取从 2 ~ 末尾 - 1的字符串
截取字符串末尾两个字符
字符串的逆序（面试题）
使用enumerate把
seasons = ['Spring', 'Summer', 'Fall', 'Winter'] 变为一个字典，效果和上课一致
"""
num_str = "0123456789"
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
def test1():
    print(num_str[2:6])
    print(num_str[2:])
    print(num_str[:5])
    print(num_str)
    print(num_str[::2])
    print(num_str[1::2])
    print(num_str[1:-1])
    print(num_str[:-3:-1])
    print(num_str[::-1])
    print(dict(enumerate(seasons)))


test1()