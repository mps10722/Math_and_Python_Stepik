rotors = {
    1: ('AELTPHQXRU', 'BKNW', 'CMOY', 'DFG', 'IV', 'JZ', 'S'),
    2: ('FIXVYOMW', 'CDKLHUP', 'ESZ', 'BJ', 'GR', 'NT', 'A', 'Q'),
    3: ('ABDHPEJT', 'CFLVMZOYQIRWUKXSG', 'N'),
    4: ('AEPLIYWCOXMRFZBSTGJQNH', 'DV', 'KU'),
    5: ('AVOLDRWFIUQBZKSMNHYC', 'EGTJPX'),
    6: ('AJQDVLEOZWIYTS', 'CGMNHFUX', 'BPRK'),
    7: ('ANOUPFRIMBZTLWKSVEGCJYDHXQ',),
    8: ('AFLSETWUNDHOZVICQ', 'BKJ', 'GXY', 'MPR'),
    'Beta': ('ALBEVFCYODJWUGNMQTZSKPR', 'HIX'),
    'Gamma': ('AFNIRLBSQWVXGUZDKMTPCOYJHE',),
}


def rotor(symbol, n, reverse=False):
    if n == 0:
        return symbol

    for i, group in enumerate(rotors[n]):
        symbol_index = group.find(symbol)

        if symbol_index > -1:
            group_index = i
            group_length = len(group)
            direction = -1 if reverse else 1

            return rotors[n][group_index][
                (symbol_index + direction) % group_length]


def reflector(symbol, n):
    pass

text = 'SOME CLEAR TEXT'
disk = 1

for ch in text:
    print(rotor(ch, disk), end='')
