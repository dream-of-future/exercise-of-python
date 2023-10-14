# 4、水仙花数是三位整数（100~999），它的各位数字立方和等于该数本身。请编写程序，实现所有水仙花数的输出。（20分）
# import math
def sxh():
    '''
    :return: sxh_list
    '''
    num = []
    start = 100
    end = 1000
    a, b, c = 0, 0, 0  # 个 十 百

    for c in range(1, 10):
        for b in range(0, 10):
             for a in range(0, 10):
                if pow(a, 3) + pow(b, 3) + pow(c, 3) == a + b*10 + c*100:
                    num.append(a + b*10 + c*100)
    return num


if __name__ == "__main__":
    ret = sxh()
    print(ret)
