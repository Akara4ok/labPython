import math
a = int(input("a = "))
if a >= 0:
    y1 = 0
    y2 = 1
    while math.fabs(y2 - y1) >= 0.0001:
        y1 = y2
        y2 = (y1 + (a/y1))/2
    res = y2
    print("res = %.5f" % (res))
else:
    print("Error")