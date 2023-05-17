a, b = list(map(int, input().split(" ")))


def gcd(x, y):
    x, y = sorted([x, y], reverse=True)  # x >= y とする

    r = x % y
    while r > 0:
        x = y
        y = r
        r = x % y

    return y


def gcd_r(x, y):
    if y > 0:
        return gcd_r(y, x % y)
    else:
        return x


print(gcd_r(a, b))
