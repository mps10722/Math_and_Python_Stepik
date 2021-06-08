from random import choice, seed


def mimic_dict(string):
    result = {}
    words = string.split()

    for i, s in enumerate(words[:-1]):
        if i == 0:
            result[''] = [s]
            result[s] = [words[i + 1]]
        else:
            if s in result:
                if words[i + 1] not in result[s]:
                    result[s].append(words[i + 1])
            else:
                result[s] = [words[i + 1]]

    return result


def print_mimic(m_dict, word=''):
    seed(41)
    result = []
    current_word = word

    for i in range(200):
        result.append(current_word)

        if current_word not in m_dict:
            current_word = ''

        current_word = choice(m_dict[current_word])

    return ' '.join(result)


print(print_mimic(mimic_dict('We are not what we should be\nWe are not what we need to be\nBut at least we are not what we used to be\n -- Football Coach''')))
