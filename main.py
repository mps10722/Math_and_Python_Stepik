from collections import deque
import re


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


enc_msg = 'ТЛБЛДУЭППТКЛФЧУВНУПБКЗИХТЛТТЫХНЛОИНУВЖММИНПФНПШОКЧЛЕРНТФНАХЖИДМ' \
          'ЯКЛТУБЖИУЕЖЕАХЛГЩЕЕЪУВНГАХИЯШПЙАОЦЦПВТЛБФТТИИНДИДНЧЮОНЯОФВТЕАТФ' \
          'УШБЛРЮЮЧЖДРУУШГЕХУРПЧЕУВАЭУОЙБДБНОЛСКЦБСАОЦЦПВИШЮТППЦЧНЖОИНШВРЗ' \
          'ЕЗКЗСБЮНЙРКПСЪЖФФШНЦЗРСЭШЦПЖСЙНГЭФФВЫМЖИЛРОЩСЗЮЙФШФДЖОИЗТРМООЙБ' \
          'НФГОЩЧФЖООКОФВЙСЭФЖУЬХИСЦЖГИЪЖДШПРМЖПУПГЦНВКБНРЕКИБШМЦХЙИАМФЛУЬ' \
          'ЙИСЗРТЕС'
keywords = {'алмаз', 'Дакоста'}

for i in range(1_000, 1_000_000):
    dec_msg = jarriquez_encryption(enc_msg, i,
                                   alphabet='АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
                                   reverse=True)
    if any(word.upper() in dec_msg for word in keywords):
        print(i, dec_msg)
