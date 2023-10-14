def bmi_guolei(bim):
    if bim < 18.5:
        return "偏瘦"
    elif bim < 24:
        return "正常"
    elif bim < 28:
        return "偏胖"
    else:
        return "肥胖"

def bmi_guoji(bim):
    if bim < 18.5:
        return "偏瘦"
    elif bim < 25:
        return "正常"
    elif bim < 30:
        return "偏胖"
    else:
        return "肥胖"

if __name__ == "__main__":
    weight = int(input("你的体重(kg):"))
    high = float(input("你的身高(m):"))
    BMI = weight / (pow(high, 2))
    ret1 = bmi_guoji(BMI)
    ret2 = bmi_guolei(BMI)
    print(f'国际标准:{ret1}\n国内标准:{ret2}')