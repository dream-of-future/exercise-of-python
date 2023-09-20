def second():
    # 输入一个浮点数，将其转换为整数，并进行输出，请采用两种函数进行转换，并通过结果分析两种函数的特点。

    flt = float(input("输入一个float:"))
    print(f"截断:{int(flt)}")
    print(f"四舍六入:{round(flt)}")

second()
