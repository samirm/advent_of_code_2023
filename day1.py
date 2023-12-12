import re


def get_numeric(number_as_str):
    valid_number_words = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    try:
        int(number_as_str)
        return number_as_str
    except ValueError:
        return valid_number_words[number_as_str]


with open('data/calibrations.txt') as file:
    lines = file.readlines()
    calibrations = []

    for line in lines:
        numbers = re.findall('(?=(one|two|three|four|five|six|seven|eight|nine|zero|\\d))', line)
        print(numbers)

        if len(numbers) == 0:
            print('No valid numbers found in this line')
        # elif len(numbers) == 1:
        #     calibrations.append(get_numeric(numbers[0]))
        else:
            calibrations.append(get_numeric(numbers[0]) + get_numeric(numbers[-1]))

    print(calibrations)
    calibrations = list(map(int, calibrations))
    print(calibrations)
    print(sum(calibrations))
