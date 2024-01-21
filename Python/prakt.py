
def reverse(x: int) -> int:
    if '-' in str(x):
        ch = str(x)[str(x).find('-'):]
        return int(ch[::-1]) * -1
    else:
        return int(str(x)[::-1])
print(reverse(-123))
        