print("n =", end=" ")
s = input()
if s.isdigit():
    n = int(s);
    n1 = n // 100
    n = (n % 100) * 10 + n1
    print("res =", n)
else:
    s = s.replace('-','')
    if s.isdigit():
        n = int(s);
        n1 = n // 100
        n = ((n % 100) * 10 + n1)*(-1)
        print("res =", n)
    else:
        print("Error")
