import random
random.seed(0x1010)

mystery = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
mystery_ls = list(mystery)
length = len(mystery_ls)
# print(length)
list1 = []
judge = []
for i in range(0, 20):
	mima = ''
	for j in range(0, 10):
		mima += mystery_ls[random.randint(0, length-1)]
	if mima[0] not in judge:
		list1.append(mima)
		judge.append(mima[0])
	if len(list1) == 10:
		break

for i in range(0,10):
	print(list1[i])
