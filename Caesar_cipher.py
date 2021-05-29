import random
import re
from collections import deque


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


def kidds_encryption(text, reverse=False):
    keys = '8;4‡)*56(1†092:3?¶.-' if reverse else 'ethosnairfdlmbyguvpc'
    values = 'ethosnairfdlmbyguvpc' if reverse else '8;4‡)*56(1†092:3?¶.-'
    dictionary = dict(zip(keys, values))
    pattern = re.compile(rf'[^{keys}]+')
    text = pattern.sub('', text.lower())

    return ''.join(dictionary[ch] for ch in text if ch in dictionary.keys())


print(kidds_encryption('ethosnairfdlmbyguvcp'))
print(kidds_encryption('8;4‡)*56(1†092:3?¶-.', True))
