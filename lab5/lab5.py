for i in range(100, 999):
    n = i
    s = 0 
    while n>0:
        s = s + (n % 10)**3
        n = n // 10
    if s==i:
        print(i)