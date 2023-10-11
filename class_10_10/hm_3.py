# （3）分别用str(iterable)、list(iterable)、tuple(iterable)、set(iterable)函数创建字符串，列表、元组以及集合，iterable为符合要求的可迭代数据类型。（15分）
str1 = str(range(10))
list1 = list(range(100,110))
tuple1 = tuple("hello")
set1 = set("python")

print(f'set={set1}\n list={list1}\n tuple={tuple1}\n str1{str1}')