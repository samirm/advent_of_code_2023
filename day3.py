import math


def size(valid_num):
    return int(math.log10(valid_num)) + 1


with open('data/test.txt') as file:
    lines = file.readlines()

    w, h = len(lines[0].strip()), len(lines)
    Matrix = [[0 for x in range(w)] for y in range(h)]

    symbol_positions = []
    number_positions_to_len_map = {}
    symbols = '+*$#'
    col = 0

    for i, i_val in enumerate(lines):
        print(i_val)
        numbers = i_val.strip().split('.')
        print(numbers)
        for number in numbers:
            if len(number) > 1:
                for c in symbols:
                    number = number.replace(c, '')
            try:
                valid_num = int(number)
            except ValueError:
                print('Not a number')

            if valid_num:
                number_positions_to_len_map.update({(i, i_val.index(str(valid_num))): size(valid_num)})
                valid_num = None
        #

        for j, j_val in enumerate(i_val.strip()):
            if j_val in '1234567890':
                Matrix[i][j] = (j_val, 'd')
            elif j_val in symbols:
                Matrix[i][j] = (j_val, 's')
                symbol_positions.append((i, j))
            else:
                Matrix[i][j] = (j_val, 'p')

    print(Matrix)
    print(symbol_positions)
    print(number_positions_to_len_map)



    for row in range(h):
        for col in range(w):
            # if Matrix[row][col][1] == 's':
            #     if Matrix[row][col-1] in '1234567890':
            #


