import info

ls = [31,28,31,30,31,30,31,31,30,31,30,31]

def is_runnian(year):
    if year % 4 == 0 and year % 100 != 0:
        return 1
    elif year % 400 == 0:
        return 1
    else:
        return 0


def how_many_day(month,day,runnian):
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
    born = input("请以形如19700101的格式输入您的生日:")
    try:
        test = int(born)
    except ValueError:
        print("输入错误，程序退出")
        exit()
    else:
        year = int(born[0:4])
        month = int(born[4:6])
        day = int(born[6:])
        print(f'Y{year} M{month} D{day}')

        if (month > 12 or day > ls[month-1]) or (month < 1 or day < 1):
            print("欢迎来到地球，天外来客\nWelcome to earth,our friend who are from space")
            print("请使用标准的地球纪年\nPlease use the standard earth's calendar")
        else:
            ret = is_runnian(year)
            if ret == 1:
                print('是闰年')
            else:
                print("不是闰年")

            ret = how_many_day(month, day, ret)
            print(f"第{ret}天")

            interesting_num(ret)