import info
def is_runnian(year):
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0


def how_many_day(month,day,runnian):
    ls = [31,28,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    for i in range(0,month-1):
        sum += ls[i]
    sum += day + runnian
    return sum


def interesting_num(num):   # 判断出生在当年的第n天是否是x的平方
    if num in [x*x for x in range(0,19)]:
        print(f'{num}这个数字很有趣')
    else:
        print(f'{num}这个数字一般有趣')

if __name__ == '__main__':
    born = input()
    try:
        test = int(born)
    except ValueError:
        print("输入错误，程序退出")
        exit()
    else:
        year = int(born[0:4])
        month = int(born[4:6])
        day = int(born[6:])
        # print(f'Y{year}M{month}D{day}')

        ret = is_runnian(year)
        if ret == 1:
            print('是闰年')
        else:
            print("不是闰年")

        ret = how_many_day(month, day, ret)
        print(f"第{ret}天")

        interesting_num(ret)