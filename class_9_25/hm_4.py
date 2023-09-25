a = '欢迎学习Python语言程序设计！'
list1 = list(a)
list1[int(input("请输入要修改的下标:"))] = input("请输入修改值:")
print(list1)