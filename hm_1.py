def sum(x, y):
    if x!=0:
       return sum((x&y)*2, x^y)
    return y
if __name__ == '__main__':
    a = int(input("請輸入1個自然數:"))
    b = int(input("請輸入1個自然數:"))
    num = sum(a,b)
    print(num)