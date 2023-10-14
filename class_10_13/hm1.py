def shiyan1():
    n = eval(input('请输入一个大于0的整数：'))
    s = 0
    for i in range(1, n + 1):
        s = i + s
    print(s)


if __name__ == '__main__':
    shiyan1()
