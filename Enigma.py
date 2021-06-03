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

shifts_at = {
    1: (17, ),
    2: (5, ),
    3: (22, ),
    4: (10, ),
    5: (0, ),
    6: (0, 13),
    7: (0, 13),
    8: (0, 13)
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


def commutator(ch, pairs):
    for pair in pairs:
        if ch in pair:
            return pair[pair.index(ch) - 1]
    else:
        return ch


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


# pairs format: 'ac BG hj'
def enigma(text, reflector_number,
           rotor_1, shift_1, rotor_2, shift_2, rotor_3, shift_3,
           pairs=''):
    pattern = re.compile(rf'[^{ALPHABET}]+')
    text = pattern.sub('', text.upper())
    pairs = [pair.upper() for pair in pairs.split()]

    if any(len(pair) != 2 or
           any(pair[0] in p or pair[1] in p
               for j, p in enumerate(pairs) if j != i)
           for i, pair in enumerate(pairs)):
        return 'Извините, невозможно произвести коммутацию'

    length_alphabet = len(ALPHABET)
    shift_at_2 = shifts_at[rotor_2]
    shift_at_3 = shifts_at[rotor_3]
    result = ''

    for ch in text:
        ch = commutator(ch, pairs)

        shift_3 = (shift_3 + 1) % length_alphabet
        rotor_3_output = rotor(rot_n(ch, shift_3), rotor_3)

        if shift_3 in shift_at_3 or shift_2 + 1 in shift_at_2:
            shift_2 = (shift_2 + 1) % length_alphabet

            if shift_2 in shift_at_2:
                shift_1 = (shift_1 + 1) % length_alphabet

        rotor_2_output = rotor(
            rot_n(rotor_3_output, shift_2 - shift_3), rotor_2)

        rotor_1_output = rotor(
            rot_n(rotor_2_output, shift_1 - shift_2), rotor_1)

        reflected = reflector(
            rot_n(rotor_1_output, -shift_1), reflector_number)

        rotor_1_output = rotor(rot_n(reflected, shift_1), rotor_1, True)

        rotor_2_output = rotor(
            rot_n(rotor_1_output, shift_2 - shift_1), rotor_2, True)

        rotor_3_output = rotor(
            rot_n(rotor_2_output, shift_3 - shift_2), rotor_3, True)

        ch = commutator(rot_n(rotor_3_output, -shift_3), pairs)

        result += ch

    return result


if __name__ == '__main__':
    import unittest
    from unittest.mock import patch
    from io import StringIO


    class Test(unittest.TestCase):

        @patch('sys.stdout', new_callable=StringIO)
        def test(self, mock_stdout):
            printed = ''
            print(enigma('A', 1, 1, 0, 2, 0, 3, 0, ''))
            printed += 'B'
            self.assertEqual(mock_stdout.getvalue(), printed + '\n')

        @patch('sys.stdout', new_callable=StringIO)
        def test2(self, mock_stdout):
            printed = ''
            print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC'))
            printed += 'Q'
            self.assertEqual(mock_stdout.getvalue(), printed + '\n')

        @patch('sys.stdout', new_callable=StringIO)
        def test3(self, mock_stdout):
            printed = ''
            print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd'))
            printed += 'D'
            self.assertEqual(mock_stdout.getvalue(), printed + '\n')

        @patch('sys.stdout', new_callable=StringIO)
        def test4(self, mock_stdout):
            printed = ''
            print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd az'))
            printed += 'Извините, невозможно произвести коммутацию'
            self.assertEqual(mock_stdout.getvalue(), printed + '\n')

        @patch('sys.stdout', new_callable=StringIO)
        def test5(self, mock_stdout):
            printed = ''
            print(enigma('A', 1, 1, 0, 2, 0, 3, 0, 'AC qd za'))
            printed += 'Извините, невозможно произвести коммутацию'
            self.assertEqual(mock_stdout.getvalue(), printed + '\n')

        @patch('sys.stdout', new_callable=StringIO)
        def test6(self, mock_stdout):
            printed = ''
            print(enigma('AAAAAAA', 1, 1, 0, 2, 0, 3, 0))
            printed += 'BDZGOWC'
            self.assertEqual(mock_stdout.getvalue(), printed + '\n')


    unittest.main()
