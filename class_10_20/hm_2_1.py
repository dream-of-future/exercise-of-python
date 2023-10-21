# （1）	在StudentInfo1函数定义时同时涉及普通位置参数，默认参数，不定长度参数（位置参数以及关键字参数），
# 其中普通位置参数涉及姓名，学号，性别，默认参数为国籍，不定长位置参数接收身高、体重，不定长关键字参数接收各科分数；

import info
def StudentInfo1(name, id, sex, country='China', *args1, **socre):
    print('姓名:', name, ', id:', id, '性别:', sex, '国家:', country, "身高体重:", args1, "各科分数:", socre)


hw = [175,70]
sc = {'英语':60,
      '高数':80,
      'python':99}
StudentInfo1("李晓明", 123456, '男', "中国", *hw, **sc)
