sl = input()
if sl[0].islower() or (sl[0].islower() and sl[1:].isupper()) or sl.isupper():
    print(sl.swapcase())
else:
    print(sl)