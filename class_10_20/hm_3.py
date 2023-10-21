# 定义一个函数 say_hi_multi_parameter，使之可接收任意数量的姓名，调用函数时，可以传递多个参数。
import info
def say_hi_multi_parameter(*name):
    lenth = len(name)
    for i in range(lenth):
        print(f'{name[i]},你好!')
    # print(type(name))

say_hi_multi_parameter("666","777")