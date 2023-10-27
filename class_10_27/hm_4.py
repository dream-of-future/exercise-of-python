import info
def add(a,n):
    num = 0
    sum = 0
    for j in range(n):
        for i in range(j+1):
            num = 10**i*a + num
        sum = sum + num
        num = 0
    return sum
ret = add(2,5)
print(ret)