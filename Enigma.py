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

reflectors = {
    # reflector B: (AY) (BR) (CU) (DH) (EQ) (FS) (GL) (IP) (JX) (KN) (MO)
    # (TZ) (VW)
    1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
    # reflector C: (AF) (BV) (CP) (DJ) (EI) (GO) (HY) (KR) (LZ) (MX) (NW)
    # (TQ) (SU)
    2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
    # reflector B Dünn: (AE) (BN) (CK) (DQ) (FU) (GY) (HW) (IJ) (LO) (MP)
    # (RX) (SZ) (TV)
    3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
    # reflector C Dünn: (AR) (BD) (CO) (EJ) (FN) (GT) (HK) (IV) (LM) (PW)
    # (QZ) (SX) (UY)
    4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'
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
    if n == 0:
        return symbol

    a_code = ord('A')
    return reflectors[n][ord(symbol) - a_code]


text = 'SOME CLEAR TEXT'
disk = 1

for ch in text:
    print(rotor(ch, disk), end='')
