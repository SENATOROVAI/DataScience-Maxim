l1 = [2,4,3]
l2 = [5,6,4]
c1 = str((int(''.join(list(map(str, l1))[::-1])) + int(''.join(list(map(str, l2))[::-1]))))
print(list(map(int,list(c1)[::-1])))
        