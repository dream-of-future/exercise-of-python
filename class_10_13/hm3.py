# 3、判断素数的程序，请将程序填写完整。（15分）
for n in range(2, 101):
    m = int(n ** 0.5)
    i = 2
    while i <= m:
        if n % i == 0:
            break
        i += 1
    if i > m:
        print(n, end=' ')
