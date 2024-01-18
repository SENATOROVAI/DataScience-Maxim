sp = [3, 2, 4]
tar = 6
s = 0
for i in range(len(sp)):
    sp1 = sp.copy()
    sp1.pop(i)
    for j in range(len(sp1)):
        if sp[i] + sp1[j] == tar:
            print([i, sp.index(sp1[j])])
            s += 1
            break
    if s == 1:
        break
