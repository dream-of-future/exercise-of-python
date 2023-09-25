def test(s):
    try:
        s[int(input("请输入要修改的下标:"))] = input("请输入修改值:")
    except TypeError as t:
        t = '无法修改字符串'
        print(t)

if __name__ == "__main__":
    str = '欢迎学习Python语言程序设计!'
    test(str)

