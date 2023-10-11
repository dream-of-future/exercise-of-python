# （4）月球上物体的体重是在地球上的16.5%，假如你在地球上每年增长0.5kg，编写程序输出未来5年（每一年的体重都输出）你在地球和月球上的体重状况。（15分）
weight = 70
g = 9.8
for i in range(1,6):
    print(f'第{i}year')
    print(f'earth:{(weight+i*0.5)*g}N\nmoon:{((weight+i*0.5)*0.165)*g}N')
