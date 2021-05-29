BASE = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843,
        1364, 2207, 3571, 5778, 9349, 15127, 24476, 39603, 64079,
        103682, 167761, 271443, 439204, 710647, 1149851,
        1860498, 3010349, 4870847, 7881196, 12752043, 20633239,
        33385282, 54018521, 87403803]


def super_l(n):
    if 0 <= n <= 38:
        return BASE[n]

    if not n % 6:
        n //= 6
        res = super_l(n)

        return (res ** 6) - (6 * (-1) ** n * res ** 4) + (9 * res ** 2) \
            - (2 * (-1) ** n)
    elif not n % 5:
        n //= 5
        res = super_l(n)

        return (res ** 5) - (5 * (-1) ** n * res ** 3) + (5 * res)
    elif not n % 4:
        n //= 4
        res = super_l(n)

        return (res ** 4) - (4 * (-1) ** n * res ** 2) + 2
    elif not n % 3:
        n //= 3
        res = super_l(n)

        return (res ** 3) - (3 * (-1) ** n * res)
    elif not n % 2:
        n //= 2
        res = super_l(n)

        return (res ** 2) - (2 * (-1) ** n)

    return BASE[n]
    

print(super_l(2 ** 20))
