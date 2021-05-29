import random
import re
from collections import deque
from typing import Any


def rot_n(text, shift, alphabet):
    alphabet = deque(alphabet)
    positions = [alphabet.index(c) for c in text]
    alphabet.rotate(-shift)
    characters = [alphabet[pos] for pos in positions]

    return ''.join(characters)


def caesar(text, key, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    pattern = re.compile(rf'[^{alphabet}]+')
    text = pattern.sub('', text.upper())

    return rot_n(text, key, alphabet)


def jarriquez_encryption(text: str, key: int,
                         alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ', reverse=False):
    pattern = re.compile(rf'[^{alphabet}]+')
    text = pattern.sub('', text.upper())
    key = [int(digit) for digit in str(key)]
    key_length = len(key)
    alphabet_length = len(alphabet)

    return ''.join(alphabet[
                       (alphabet.index(ch) + key[i % key_length]
                        * (-1 if reverse else 1)) % alphabet_length
                       ] for i, ch in enumerate(text))


def disc_generator(alphabet):
    result = list(alphabet)
    random.shuffle(result)

    return ''.join(result)


def jefferson_encryption(text: str, discs: list, step: int, reverse=False):
    discs_count = len(discs)
    pattern = re.compile(rf'[^{discs[0]}]+')
    text = pattern.sub('', text.upper())

    return "".join([rot_n(ch, step * (-1 if reverse else 1),
                          discs[i % discs_count])
                    for i, ch in enumerate(text)])


random.seed(42)

clear_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n = 6
txt = 'Some encripted text'

discs_list: Any = [list(clear_alphabet) for _ in range(n)]

for index, disc in enumerate(discs_list):
    random.shuffle(disc)
    discs_list[index] = ''.join(discs_list[index])

print(f'Enc: {jefferson_encryption(txt, discs_list, 4)}')
print('Dec: ' + jefferson_encryption("NUXHUEVGQBIJJZNVI", discs_list, 4, True))
