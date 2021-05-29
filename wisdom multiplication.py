def export_to_html(data):
    # Открытие файла index.html для записи html
    with open('index.html', mode='w', encoding='utf-8') as file:
        # Функция проверяет первый индекс в каждом tuple и в зависимости от
        # результата возвращает цвет фона и текста в виде строки css стиля
        def colorize(val):
            color = ''
            bgc = ''

            if val[0] == 0:  # 0 - правильный результат с проверкой на '0'
                color = '#fff'
                bgc = '#aa5900'  # 0 - оранжевый (почти) цвет
            elif val[0] == 1:  # 1 - правильный результат
                color = '#fff'
                bgc = '#006000'  # 1 - зелёный цвет
            elif val[0] == -1:  # -1 - неправильный результат
                color = '#fff'
                bgc = '#900000'  # -1 - красный цвет

            return f'color: {color}; background-color: {bgc};'

        result = pd.DataFrame(data)

        # Заголовок таблицы с описанием цветов.
        # span'ы собраны в div'ы, чтобы каждый пункт начинался на новой строке
        # float: left у первого span'а сделан, чтобы к нему "прилипал"
        # span справа, иначе текст уезжает вниз

        # Неправильные результаты:
        caption = '<div style="margin: 0.5em 0;">' \
                  '<span style="display: inline-block; width: 1.5em; ' \
                  'height: 1.5em; float: left; background-color: #900000;">' \
                  '</span>' \
                  '<span style="display: inline-block; ' \
                  'height: 1.5em; margin-left: 0.5em;">' \
                  ' - неправильные результаты' \
                  '</span>' \
                  '</div>'

        # Правильные результаты:
        caption += '<div style="margin: 0.5em 0;">' \
                   '<span style="display: inline-block; width: 1.5em; ' \
                   'height: 1.5em; float: left; background-color: #006000;">' \
                   '</span>' \
                   '<span style="display: inline-block; height: '\
                   '1.5em; margin-left: 0.5em;">' \
                   ' - правильные результаты' \
                   '</span>' \
                   '</div>'

        # Правильные результаты (с проверкой на разделитель '0'):
        caption += '<div style="margin: 0.5em 0;">' \
                   '<span style="display: inline-block; width: 1.5em; ' \
                   'height: 1.5em; float: left; background-color: #aa5900;">' \
                   '</span>' \
                   '<span style="display: inline-block; height: 1.5em; '\
                   'margin-left: 0.5em;"> ' \
                   '- правильные результаты ' \
                   '(с проверкой на разделитель \'0\')' \
                   '</span>' \
                   '</div>'

        # Стили для th ячеек (заголовков строк и столбцов)
        th_props = [
            ('padding', '5px'),
            ('font-weight', 'bold'),
            ('color', '#aaa'),
            ('background-color', '#333'),
            ('border', '1px solid #ddd')
        ]

        # Стили для td (всех ячеек кроме th)
        td_props = [
            ('padding', '5px'),
            ('border', '1px solid #ddd'),
            ('transition', 'box-shadow .25s, text-shadow .25s, border .25s')
        ]

        # Стили для заголовка таблицы
        caption_props = [
            ('text-align', 'left'),
            ('font-weight', 'bold')
        ]

        # Собирание всех втилей в один list
        styles = [
            # При наведении курсором на строку, все буквы становятся жирными
            dict(selector='tr:hover', props=[('font-weight', 'bold'),
                                             ('color', '#fff'),
                                             ('cursor', 'pointer')]),
            # Так же у ячейки, находящейся в данный момент, под курсором
            # добавляется тень для текста и тень для границ ячейки
            dict(selector='td:hover', props=[('text-shadow',
                                              '-1px 0 black, 0 1px black,'
                                              ' 1px 0 black, 0 -1px black'),
                                             ('-moz-box-shadow',
                                              'inset 0 0 10px #000'),
                                             ('-webkit-box-shadow',
                                              'inset 0 0 10px #000'),
                                             ('box-shadow',
                                              'inset 0 0 10px #000'),
                                             ('border',
                                              '1px solid #000')]),
            dict(selector='th', props=th_props),
            dict(selector='td', props=td_props),
            # Подсветка числа (результата) для лучшей читабельности
            dict(selector='td span.result', props=[('color', '#0ff')]),
            dict(selector='caption', props=caption_props)
        ]

        # set_caption - Подключение заголовка таблицы, настроенного ранее
        # applymap - Раскрашивание ячейки с помощью
        # ранее определённой функции colorize
        # set_table_styles - Подключение стилей, собранных в переменную styles
        # set_table_attributes - Настройка стилей тега table
        # format - отфильтровать ненужную цифру-флаг в tuple
        # Например для (-1, '82x91 73162') результат будет '82x91 73162'
        # render - как я понял (не знаком с pandas)
        # компилирует DataFrame + стили в str содержащую html код
        result = result\
            .style \
            .set_caption(caption)\
            .applymap(colorize)\
            .set_table_styles(styles)\
            .set_table_attributes('style="border-collapse: collapse; '
                                  'text-align: center;"')\
            .format(lambda x: x[1])\
            .render()

        # Добавление тегов html body и кодировки utf-8 чтобы русские буквы
        # правильно отображались
        html = ' <!DOCTYPE html>' \
               '<html>' \
               '<head><meta charset="utf-8"></head>' \
               '<body ' \
               'style="margin: 0; padding: 0.5em; background-color: #ddd;' \
               'font-family: Courier, sans-serif">' \
               + result \
               + '</body>' \
                 '</html>'

        # Запись в файл готового html
        file.write(html)


def wisdom_multiplication_list(start=10, stop=99):
    # Счетчики неправильных, правильных и
    # правильных с проверкой на '0' результатов
    negative = positive = zero_check = 0

    # Структура словаря такая (для 82x91):
    # data = {82: {91: (-1, 73162)}}
    data = {}

    # Цикл строк
    # Начинается со start - 1, чтобы выводить заголовок строки
    for i in range(start, stop + 1):
        # Если i больше или равен start - создаётся пустой словарь
        # для последующего использования
        data[i] = {}

        # Цикл столбцов
        for j in range(start, stop + 1):
            # Результом вызова функции wisdom_multiplication является:
            # tuple(bool, bool, int), где:
            # первый bool - Если True, то результат был дополнен '0'
            # второй bool - Если True, то результат правильный
            # третий int - результат умножения i на j
            result = wisdom_multiplication(i, j)

            # Формирование строки, которая будет записана в ячейку таблицы
            val = f'{i}x{j}<br><span class="result">{result[2]}</span>'

            # Заполнение структуры data для DataFrame
            # В data[i][j] записывается tuple, первый int которого, является
            # флагом для дальнеёшего раскрашивания ячеек. Я использовал такой
            # способ так как не знаю как правильно раскрасить ячейки.

            # Если результат был дополнен нулём и является правильным
            if result[0] and result[1]:
                zero_check += 1
                data[i][j] = (0, val)
            # Если результат правильный, без дополнения
            elif result[1]:
                positive += 1
                data[i][j] = (1, val)
            # Если результат неправильный
            else:
                negative += 1
                data[i][j] = (-1, val)

    # Консольные результаты из прошлых заданий (не мешают, пусть будут)
    print(f'Правильных результатов: {positive}\n'
          f'Правильных результатов (с проверкой на ноль): {zero_check}\n'
          f'Неправильных результатов: {negative}')

    export_to_html(data)


def wisdom_multiplication(x, y):
    a = 100 - x
    b = 100 - y

    # Левая часть числа: 100 - ((100 - x) + (100 - y))
    left_part = 100 - (a + b)

    # Правая часть числа: (100 - x) * (100 - y)
    right_part = a * b

    # Флаг указывающий, что результат был дополнен '0'
    is_zero_padded = False

    # Если правая часть однозначная то дополняется '0' до двузначной
    if right_part < 10:
        is_zero_padded = True
        right_part = f'0{right_part}'

    result = int(f'{left_part}{right_part}')

    # Возвращается tuple с:
    # - (bool) дополнен ли рузультат '0'
    # - (bool) правильный ли результат
    # - (int) результат
    return is_zero_padded, result == x * y, result


if __name__ == '__main__':
    import pandas as pd

    wisdom_multiplication_list()
