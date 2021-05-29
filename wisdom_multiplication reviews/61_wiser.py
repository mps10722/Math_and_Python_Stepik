import pandas


# function, which execute wisdom multiplication and compares it with classic multiplication.
def wisdom_multiplication(x, y):
    first_part = str(100 - (100 - x) - (100 - y))
    second_part = str((100 - x) * (100 - y))
    result = first_part + second_part
    result_with_zero = first_part + '0' + second_part
    if int(result) == (x * y):
        return 2
    elif int(result_with_zero) == (x * y):
        return 1
    else:
        return 0


# function that adds pairs of numbers, for which wisdom multiplication is applicable, to 2 lists
def multiplication_check_list(start=10, stop=99):
    wisdom_works = []
    wisdom_works_with_zero = []
    for i in range(start, stop + 1):
        for j in range(start, stop + 1):
            if wisdom_multiplication(i, j) == 2:
                wisdom_works.append(str(i) + '*' + str(j))
            elif wisdom_multiplication(i, j) == 1:
                wisdom_works_with_zero.append(str(i) + '*' + str(j))
    return wisdom_works, wisdom_works_with_zero


# Style function.Set custom background for cells
def highlight_wisdom_cells(value, wisdom_works_list: list, wisdom_works_zero_list: list):
    if value in wisdom_works_list:
        return 'background: green'
    elif value in wisdom_works_zero_list:
        return 'background: yellow'
    else:
        return 'background: white'


# function to set borders for each cell in table
def border(val):
    return 'border: 1px solid black'


# list1 includes pairs of numbers, for which wisdom multiplication is applicable.
# list 2 includes pairs of numbers, for which wisdom multiplication is applicable after zero adding
list1, list2 = multiplication_check_list()

# list of all numbers 10..99x10..99 for data frame creation
list_for_table = [[str(i) + '*' + str(j) for i in range(10, 100)] for j in
                  range(10, 100)]

data_frame = pandas.DataFrame(list_for_table,
                              index=[i for i in range(10, 100)],
                              columns=[j for j in range(10, 100)])

# styler object with applied styles from functions "highlight_wisdom_cells" and "border"
styler = data_frame.style.applymap(highlight_wisdom_cells, wisdom_works_list=list1, wisdom_works_zero_list=list2).applymap(border)

with open('61_filename.html', 'w') as html:
    # styler.render() returns HTML code
    html.write(styler.render())
