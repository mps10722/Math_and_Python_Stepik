import re

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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


def rot_n(ch, shift):
    symbol_index = ALPHABET.find(ch)

    if symbol_index > -1:
        return ALPHABET[(symbol_index + shift) % len(ALPHABET)]


def enigma(text, ref, rotor_1, shift_1, rotor_2, shift_2, rotor_3, shift_3):
    pattern = re.compile(rf'[^{reflectors[1]}]+')
    text = pattern.sub('', text.upper())
    shifted = 0
    result = ''

    for ch in text:
        rotor_3_output = rotor(rot_n(ch, shift_3), rotor_3) \
            if rotor_3 > 0 else ch

        rotor_2_output = rotor(
            rot_n(rotor_3_output, shift_2 - shift_3), rotor_2) \
            if rotor_2 > 0 else rotor_3_output

        rotor_1_output = rotor(
            rot_n(rotor_2_output, -shift_2 + shift_3),
            rotor_1) if rotor_1 > 0 else rotor_2_output

        reflected = reflector(rot_n(rotor_1_output, -shift_1), ref)

        rotor_1_output = rotor(rot_n(reflected, shift_1), rotor_1, True) \
            if rotor_1 > 0 else reflected
        rotor_2_output = rotor(
            rot_n(rotor_1_output, shift_2 - shift_1), rotor_2, True) \
            if rotor_2 > 0 else rotor_1_output
        rotor_3_output = rotor(
            rot_n(rotor_2_output, -shift_2 + shift_3), rotor_3, True) \
            if rotor_3 > 0 else rotor_2_output

        result += rot_n(rotor_3_output, -shift_3)

    return result
