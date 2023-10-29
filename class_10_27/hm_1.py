import info
def test_xh():  # 循环实现（偷个懒，就不分文件了）
    def peach(num):
        return (num + 1) * 2
    day = 10
    num = 1
    print(f'第{day}天有{num}只桃子')
    while (day > 1):
        num = peach(num)
        day -= 1
        print(f'第{day}天有{num}只桃子')


def peach(day,last_day):
    if day == last_day:
        return 1
    else:
        return (2*(peach(day+1,last_day)+1))
if __name__ == '__main__':
    for i in range(1,11):
        ret = peach(11-i,10)
        print(f'第{11-i}天有{ret}只桃子')
    # test_xh()