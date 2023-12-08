s = '''
"Collusion is very real with Russia," Trump quoted conservative commentator Dan Bongino as saying on Trump's favorite Fox News morning show, "but only with Hillary and the Democrats, and we should demand a full investigation."
'''
ls1 = s.replace("\"", ' ',-1)
# print(ls1)
ls2 = ls1.replace(',', ' ')
# print(ls2)
ls3 = ls2.split()

# print(ls3)
print(len(ls3))
# 这段句子输入太规范了，可以直接.split()解
