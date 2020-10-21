n = int(input())
if n>0:
    n1 = n // 100
    n = (n % 100) * 10 + n1
else:
    n1 = ((-1) * n) // 100
    n = ((((-1) * n) % 100) * 10 + n1)*(-1)
print(n)
