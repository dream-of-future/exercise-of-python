# 1、基本知识点练习（15分）
# （1） 用5种方式创建字典，字典内容为大家上学期任选5门课程的成绩，如{“英语”：80，”体育”：100，”模电”：89，”数电”：78，”测控电路”：76}
cj = {'c程序设计理论':99, 'c程序设计实验':96,'英语':80,'体育':90,'电工':80 }
cj2 = dict(c程序设计理论=99, c程序设计实验=96, 英语=80, 体育=90, 电工=80)
cj3 = dict(zip(('c程序设计理论','c程序设计实验', '英语', '体育', '电工'),(99, 96, 80, 90, 80)))
cj4 = dict([('c程序设计理论',99),('c程序设计实验',96),('英语',80),('体育',90),('电工',80)])
cj5 = dict(cj)
print(cj.values())
print(cj.keys())
# print(cj3)
print(cj,cj2,cj3,cj4,cj5,sep="\n")