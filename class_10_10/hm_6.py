# 1、用户输入的一个整数N，输出N中所出现不同数字的和。（10分）
# 例如：用户输入123123123，其中所出现的不同数字为：1、2、3，这几个数字和为6。
# 示例1：‬
# 输入：
# 123123123
# 输出：
# 6
def fun1(str1):  # list储存法
    """
    :param str1: 传入一个内部为int的str
    :return 不同数字相加后的值
    """
    num = []
    # len1 = len(str1)
    for i in str1:
        if i not in num:
            num.append(i)
    len2 = len(num)
    add = 0
    for i in range(len2):
        add = add + int(num[i])
    return add


def fun2(list1):  # 删除法
    """
    :param list1:传入一个内部为int的list
    :return: 不同数字相加后的值
    """
    num = []
    while(len(list1)!=0):
        if list1[0] not in num:
            num.append(list1[0])
        del list1[0]
    add = 0
    len2 = len(num)
    for i in range(len2):
        add = add + int(num[i])
    return add


def fun3(str1):  # set法
    set1 = set(list(str1))
    num = list(set1)
    add = 0
    len2 = len(num)
    for i in range(len2):
        add = add + int(num[i])
    return add


str1 = input("输入一个内部为int的str:")
list1 = list(str1)
ret2 = fun2(list1)
ret1 = fun1(str1)
ret3 = fun3(str1)
print(ret1,ret2,ret3,sep='\n')
