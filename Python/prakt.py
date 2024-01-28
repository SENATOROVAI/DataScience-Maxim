def isValid(s: str):
    sl: dict = {}
    for i in s:
        sl[i] = sl.get(i, 0) + 1
    if sl['('] == sl[')'] and sl['['] == sl[']'] and sl['{'] == sl['}']:
        return True
    else:
        return False
print(isValid('()[]{}}'))