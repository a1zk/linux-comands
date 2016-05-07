import sys

x = float(sys.argv[1]) #1st argument
y = float(sys.argv[2]) # 2nd argument

import math

f = (math.sqrt(x * y) / (math.exp(x) * y)) + (x * math.exp(2 * x / y))
print(f)
