import timeit

stmt_1 = '''
KAPREKAR_NUMBERS = [1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4879, 4950,
                    5050, 5292, 7272, 7777, 9999, 17344, 22222, 38962, 77778,
                    82656, 95121, 99999, 142857, 148149, 181819, 187110,
                    208495, 318682, 329967, 351352, 356643, 390313, 461539,
                    466830, 499500, 500500, 533170]
ALPHAS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


def convert(num, to_base=10, from_base=10) -> str:
    if to_base == 10:
        return str(int(num))

    num = str(num)
    dec = int(num, from_base)
    result = []

    while dec >= to_base:
        remainder = dec % to_base
        dec //= to_base
        result.insert(0, ALPHAS[remainder])

    result.insert(0, ALPHAS[dec])

    return ''.join(result)


def split_number(number: int, base=10):
    number_str = convert(number, to_base=base)
    number_str_len = len(number_str)

    return [(int(number_str[:i], base), int(number_str[i:], base))
            for i in range(1, number_str_len)
            if int(number_str[:i], base) > 0 and int(number_str[i:], base) > 0]


def kaprekar(number, base=10):
    if base == 10 and number in KAPREKAR_NUMBERS:
        return True

    number = str(number)

    number_pairs = split_number(int(number, base) ** 2, base)

    for a, b in number_pairs:
        if convert(a + b, to_base=base) == number:
            return True

    return False


x = kaprekar('CF97C', 16)
'''

stmt_2 = '''
def partition(n, base):
    i = 1
    f, s = divmod(n, base)
    while f:
        yield f, s
        i *= base
        f, k = divmod(f, base)
        s += i * k

def kaprekar(n, base=10):
    n = int(n, base)
    sq = n**2
    return any(n - f == s != 0 for f, s in partition(sq, base))
    

x = kaprekar('CF97C', 16)
'''

print('My:', timeit.timeit(stmt_1, number=100_000))
print('Dmitry Sokolov:', timeit.timeit(stmt_2, number=100_000))
