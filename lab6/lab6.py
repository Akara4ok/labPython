def GCD(a, b):
    return a if (b == 0) else GCD(b, a % b)

n = int(input("n = "))
i = int(input("i = "))
m = int(input("m = "))

print("GCD =", GCD(n, GCD(i, m)))