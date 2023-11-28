import info
'''
2. 输入一组数字，采用逗号分隔，输出其中的最大值。（10分）
输入："8,3,5,7"
输出："8"
'''


get = input()
arr = eval('['+get+']')

# arr = ''.join(get)
Max = max(arr)
print(Max)