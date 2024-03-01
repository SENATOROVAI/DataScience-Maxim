def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    # if base > len(digits): return ''
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result
n = int(input())
sp = []
for i in range(2, n):
    sp.append(sum(list(map(lambda x: int(x) if x.isdigit() else 0,convert_to(n, i)))))
print(f'{sum(sp)}/{n - 2}')
                