# （2）用实例证明集合数据类型：（15分）
# 1）不能含有重复元素；
# 2）不能含有可变数据类型元素。
# 提示：自己定义集合元素，截图报错信息。
def test1():
    try:
        s = set(1, 1, 1, 666, 5)
    except TypeError:
        print('TypeError集合元素重复')
    else:
        print('s没错')

def test2():
    a = 100
    b = 562
    c = [56, 8, 9]
    d = (56, 85, 32, 7)

    try:
        e = {a, b, d}
    except TypeError:
        print("e2有TypeError: unhashable type: 'list'")
    else:
        print("e没错")

    try:
        e1 = {a, b, c, d}
    except TypeError:
        print("e1有TypeError: unhashable type: 'list'")
    else:
        print("e1没错")
if __name__ == "__main__":
    test1()
    test2()