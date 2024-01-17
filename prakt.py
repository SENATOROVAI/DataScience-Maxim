def iscl(x):
    if x % 3 == 0 and str(x)[-1] != '4' and str(x)[-1] != '7':
        return True
    else:
        return False
print(sum(filter(iscl, list(range(1, 1000000003)))))