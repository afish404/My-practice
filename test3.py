# 3、通过try进行异常捕捉，确保输入的内容一定是一个整型数，
# 然后判断该整型数是否是对称数，12321就是对称数，
# 123321也是对称数，否则就打印不是，非整型抛异常，不是对称数抛异常

def mirror_num():
    raw = input('please input an integer:')
    num = int(raw)
    if(raw != raw[::-1]):
        raise Exception('not a mirror number')
    return num

if __name__ == '__main__':
    try:
        mirror_num()
    except ValueError:
        print("invalid")
    except Exception as e:
        print(e)
    else:
        print('true')