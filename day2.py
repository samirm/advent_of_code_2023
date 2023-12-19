from enum import Enum
import math


class Colour(Enum):
    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'


def determine_if_valid(cubes, total_cubes):
    if cubes[1].strip() == Colour.BLUE:
        total_cubes[Colour.BLUE] = total_cubes[Colour.BLUE] - int(cubes[0].strip())
    elif cubes[1].strip() == Colour.RED:
        total_cubes[Colour.RED] = total_cubes[Colour.RED] - int(cubes[0].strip())
    elif cubes[1].strip() == Colour.GREEN:
        total_cubes[Colour.GREEN] = total_cubes[Colour.GREEN] - int(cubes[0].strip())

    return total_cubes[Colour.BLUE] >= 0 and total_cubes[Colour.RED] >= 0 and total_cubes[Colour.GREEN] >= 0
    # valid_games.append(int(game_id))


def get_max(cube_pairs, max):
    for cube in cube_pairs:
        cubes = cube.strip().split(' ')
        number = int(cubes[0].strip())
        colour = cubes[1].strip()
        match colour:
            case Colour.BLUE.value:
                if max[Colour.BLUE] < number:
                    max[Colour.BLUE] = number
            case Colour.RED.value:
                if max[Colour.RED] < number:
                    max[Colour.RED] = number
            case Colour.GREEN.value:
                if max[Colour.GREEN] < number:
                    max[Colour.GREEN] = number
            case _:
                print('Default case, something went wrong.')

    return max


with open('data/games.txt') as file:
    lines = file.readlines()
    valid_games = []
    invalid_games = []
    all_games = {}

    for line in lines:
        game_data = line.split(':')
        game_id = game_data[0].split(' ')[1]
        sets = game_data[1].split(';')
        all_games.update({game_id: (sets, True)})

    for game_id, sets in all_games.items():
        if not sets[1]: continue
        print('Game data: \n')
        print(game_id)
        print(sets)
        print('---\n')

        for this_set in sets[0]:
            cube_pairs = this_set.split(',')
            for cube in cube_pairs:
                cubes = cube.strip().split(' ')
                total_cubes = {
                    Colour.BLUE: 14,
                    Colour.RED: 12,
                    Colour.GREEN: 13
                }
                if not determine_if_valid(cubes, total_cubes):
                    all_games.update({game_id: (sets[0], False)})
                    break

    print('Results part 1: ')
    for game_id, sets in all_games.items():
        if sets[1]:
            valid_games.append(int(game_id))
    print(valid_games)
    print(sum(valid_games))

    print('\n===============\n')
    powers = []

    for game_id, sets in all_games.items():
        max = {Colour.RED: 0, Colour.GREEN: 0, Colour.BLUE: 0}

        for this_set in sets[0]:
            cube_pairs = this_set.split(',')
            # print(cube_pairs)
            max = get_max(cube_pairs, max)

        all_games.update({game_id: (sets[0], max)})
        # print(all_games)

    for game in all_games.values():
        powers.append(math.prod(list(game[1].values())))

    print('Results part 2: ')
    print(powers)
    print(sum(powers))