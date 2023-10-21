import info
def StudentInfo1(name, *args):
    print('姓名:', name, ", 其他:", args)


def StudentInfo2(name, **args):
    print('姓名:', name, ", 其他:", args)


def StudentInfo3(name, *args, country='中国'):
    print('姓名:', name, ", 国家:", country, ", 其他:", args)


StudentInfo1("李晓明", "良好", "中国")
StudentInfo2("李晓明", 中文水平="良好", 国家="中国")
StudentInfo3("李晓明", 19, "良好")
StudentInfo3("大卫", 19, "良好", country='美国')