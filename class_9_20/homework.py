def first():
    '''
    输入一个自然数，输出它的二进制、八进制、十六进制表示形式。
    '''
    a = input("输入一个int:")
    print(f"十进制{int(a)}")
    num = int(a)
    print(f"bin：{bin(num)}")
    print(f"八进制{oct(num)}")
    print(f"16进制{hex(num)}")

first()
