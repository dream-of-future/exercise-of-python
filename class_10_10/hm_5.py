# 2、程序的修改与调试（30分）
# 货币转换：
# 人民币和美元是世界上通用的两种货币之一，写一个程序进行货币间币值转换，其中：人民币和美元间汇率采用最新汇率。‬
# 程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格。
# 示例1：‬
# 输入："RMB123"
# 输出："USD18.14"
# 示例2：‬
# 输入："USD20"
# 输出："RMB135.60"

rd = 0.14  # rmb-->dollar = 1:0.14
money = input("请输入带有符号的货币值: ")

if money[0:3] == 'rmb' or money[0:3] == 'RMB':
    dollar = (eval(money[3:]))*rd
    print(f"USD{dollar}")

elif money[0:3] == 'usd' or money[0:3] == 'USD':
    rmb = (eval(money[3:]))/rd
    print(f'RMB{rmb}')

else:
    print("输入格式错误")
