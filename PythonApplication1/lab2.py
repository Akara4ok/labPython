print("r =", end=" ")
r = int(input())
print("s =", end=" ")
s = int(input())
print("a =", end=" ")
a = int(input())
print("b =", end=" ")
b = int(input())

if (a>=0) and (b>0):
    c = a % b
    if c == r:
        print("Yes")
    elif c == s:
        print("Yes")
    else:
        print("No")
else:
    print("Error")
