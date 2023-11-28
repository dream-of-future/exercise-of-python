import info
d = {"北京大学":"北京",
     "中国人民大学":"北京",
     "清华大学":"北京",
     "北京航空航天大学":"北京",
     "北京理工大学":"北京",
     "中国农业大学":"北京",
     "北京师范大学":"北京",
     "中央民族大学":"北京",
     "南开大学":"天津",
     "天津大学":"天津",
     "大连理工大学":"辽宁","吉林大学":"吉林",\
"哈尔滨工业大学":"黑龙江","复旦大学":"上海", "同济大学":"上海",\
"上海交通大学":"上海","华东师范大学":"上海", "南京大学":"江苏",\
"东南大学":"江苏","浙江大学":"浙江","中国科学技术大学":"安徽",\
"厦门大学":"福建","山东大学":"山东", "中国海洋大学":"山东",\
"武汉大学":"湖北","华中科技大学":"湖北", "中南大学":"湖南",\
"中山大学":"广东","华南理工大学":"广东", "四川大学":"四川",\
"电子科技大学":"四川","重庆大学":"重庆","西安交通大学":"陕西",\
"西北工业大学":"陕西","兰州大学":"甘肃", "国防科技大学":"湖南",\
"东北大学":"辽宁","郑州大学":"河南", "湖南大学":"湖南", "云南大学":"云南", \
"西北农林科技大学":"陕西", "新疆大学":"新疆"}

all_city = '北京市，天津市，上海市，重庆市，河北省，山西省，辽宁省，吉林省，黑龙江省，江苏省，浙江省，安徽省，福建省，江西省，山东省，河南省，湖北省，湖南省，广东省，海南省，四川省，贵州省，云南省，陕西省，甘肃省，青海省，台湾省，内蒙古自治区，广西壮族自治区，西藏自治区，宁夏回族自治区，新疆维吾尔自治区，香港特别行政区，澳门特别行政区'

city = []
num = 0
num_university=[]
for i in list(d.values()):
    # print(i)
    if i not in city:
        city.append(i)

for i in city:
    num = 0
    for j in list(d.values()):
        if i == j:
            num += 1
    num_university.append([i, num])


def Print(list1):
    lenth = len(list1)
    for i in range(lenth):
        print(f'{list1[i][0]}:{list1[i][1]}')


university = list(set(d.keys()))
def Print_university(dic,key):
    school = []
    for i in list(dic.keys()):
        if dic[i] == key:
            school.append(i)
    if school[0] != '':
        print(school)
    else:
        print('该省份无双一流高校')


if __name__ == '__main__':
    get = input()
    if get == '':
        Print(num_university)
    elif '大学' in get or "学院" in get:
        if get in university:
            print('是双一流大学')
        else:
            print("不是双一流大学")
    elif get in all_city:
        if get in city:
            Print_university(d,get)
        else:
            print('该省份无双一流高校')

    elif get == '以省命名的高校':
        academy = []
        for i in city:
            if i+'大学' in university:
                academy.append(i+'大学')
        print(academy)

    else:
        print('输入错误')
    