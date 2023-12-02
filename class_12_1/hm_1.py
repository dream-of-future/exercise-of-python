import info
import random

random.seed(175)
N = int(input())
for i in range(0,3):
    rd = random.randint(10**(N-1),10**N)
    print(rd)