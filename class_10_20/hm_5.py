import info
import sys
from hm_4 import pell
if len(sys.argv) > 1:
    ret = pell(int(sys.argv[1]))
else:
    ret = pell(int(input()))
# import hm_4
# ret = hm_4.pell(int(input()))
print(ret)
