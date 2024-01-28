from typing import List
sp = [2, 3, 8, 6, 45, 32, 56, 32, 14, 25]
sp1 = [0]
[2, 5, 13, 19, 64, 96, 152, 184, 198, 223]

sp2: List = [sum(sp[:i]) + sp[i + 1] for i in range(len(sp))]
for i in range(len(sp)):
    sp1.append(sp[i] + sp1[i])
sp1.pop(0)
