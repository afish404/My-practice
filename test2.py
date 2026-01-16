#2.完成文件的文本模式的读，写（与上课一致）

open('file.txt', 'w', encoding='utf-8').write('内极乐世界的数据服务器群一般不是凡人能亲眼见见的。当然，现在也谈不上“凡人”了。那些服务器藏在冰岛冰冷的地下、沙漠深处被遗忘的掩体里，或者干脆就是海底缆线交汇处膨胀出的硅基珊瑚礁。它们吞吐的是电，是光，是脱离了肉身、被编码成信息洪流的“灵魂”。自从“彼岸”上线，意识上传成了新纪元最时髦的死亡——或者说，永生。')

def open_r():
    file1 = open('file.txt','r',encoding='utf8')
    text = file1.read(5)
    print(text)
    file1.close()

def open_w():
    file2 = open('file.txt','w',encoding='utf8')
    file2.write('赵一明属于最后一批“原生人”，物理意义上那种。倒不是他有多眷恋血肉之躯，纯粹是因为他那倒霉的、不可修复的神经缺陷，让他在上传扫描仪面前像个信号黑洞，扫描十次，失败十次。他被遗弃在了这个日渐空旷的物理世界，成了管理员，看守着第三区一处中等规模的意识服务器节点——一个位于废弃城市边缘，伪装成普通物流仓库的灰色建筑。')
    file2.close()

def open_a():
    file3 = open('file.txt','a',encoding='utf8')
    text = file3.write('他的日常，就是穿着静电服，穿过嗡嗡作响、蓝光流淌的服务器矩阵，检查那些冰冷的金属柜体上跳跃的、代表数十万“彼岸”居民思维活跃度的绿色数据流。今天，那些数据流似乎……有点过于整齐了。')
    file3.close()

def open_r2():
    file4 = open('file.txt','r+',encoding='utf8')
    text = file4.write('他停下脚步，揉了揉发涩的眼睛。不是错觉。往常，那些光点跳跃闪烁，带着各自生命独有的韵律，像一片纷繁的电子星海。可现在，它们起伏的节奏，波峰与波谷，甚至细微的颤动模式，都呈现出一种诡异的同步。单调，精确，像一台巨大无比的机器在规律地呼吸。')
    print(text)
    file4.close()

def open_a2():
    file5 = open('file.txt','a+',encoding='utf8')
    text = file5.write('一股寒意顺着赵一明的脊椎爬上来。他快步走到最近的监控终端，手指在冰冷的触摸屏上飞快滑动，调出深层意识活性分析图表。图表展开的瞬间，他的呼吸停滞了。')
    print(text)
    file5.close()
    
def open_rb():
    file6 = open('novel.png','rb')
    picture = file6.read()
    file6_2 = open('novel2.png','wb')
    file6_2.write(picture)
    file6_2.close
    file6.close

if __name__ == '__main__':
    open_r()
    open_w()
    open_a()
    open_r2()
    open_a2()
    # open_rb()