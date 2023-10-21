import info
def pell(num):
    if num >=2:
        pell_num = [0, 1]
        for i in range(2, num):
            pell_num.append(pell_num[i - 1] * 2 + pell_num[i - 2])
        return pell_num
    elif num==1:
        return 0
    else:
        print('输入错误')
        exit(0)

if __name__ == "__main__":
    ret = pell(int(input()))
    print(ret)
