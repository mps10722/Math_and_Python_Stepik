import os
from sys import stdout


def numerics(number: int, limit: int = 4) -> str:
    result = str(number)

    if len(result) < limit:
        result += '0' * (limit - len(result))

    return result


def kaprekar_check(number: int) -> [bool, int]:
    length = len(str(number))

    if length not in [3, 4, 6] or len(set(str(number))) == 1 \
            or number in [100, 1_000, 100_000]:
        print(f'Ошибка! На вход подано число {number}, '
              f'не удовлетворяющее условиям процесса Капрекара')

        return False, -1

    return True, length


def kaprekar_step(digits: str) -> int:
    a = ''.join(sorted(digits))
    b = int(''.join(reversed(a)))

    return abs(int(a) - b)


def kaprekar(number: int) -> [int, int]:
    prev = 0
    count = 0
    check = kaprekar_check(number)
    limit = check[1]
    seen = set()

    if not check[0]:
        exit(0)

    stdout.write('In progress...\n')
    while prev != number:
        if number in seen:
            stdout.write('\033[1G\033[K')
            stdout.write(f'Следующее число - {number}, '
                         f'кажется процесс зациклился...')
            stdout.flush()

            exit(0)

        count += 1
        stdout.write('\033[1G\033[K')
        stdout.write(f'Current number: {number}, iterations: {count}')
        stdout.flush()

        digits = numerics(number, limit)

        prev = number
        seen.add(number)
        number = kaprekar_step(digits)

    return number, count


if __name__ == '__main__':
    os.system('cls')
    res = kaprekar(int(input()))
    stdout.write('\033[1G\033[K')
    stdout.write(f'Results:\nNumber: {res[0]}, iterations: {res[1]}')
    stdout.flush()
