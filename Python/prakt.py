n = int(input())
c = 0
for i in range(5, 0, -1):
    while n - i >= 0:
        n -= i
        c += 1
print(c)