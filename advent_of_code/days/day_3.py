import csv

# https://adventofcode.com/2020/day/3

def main():
    my_input = []
    with open('advent_of_code/input/day_3.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            my_input.append(row[0])
    
    trees_encountered_3_1 = count_trees_encountered(my_input, (3, 1))
    print("Number of trees encountered: {}".format(trees_encountered_3_1))

    trees_encountered_1_1 = count_trees_encountered(my_input, (1, 1))
    trees_encountered_3_1 = count_trees_encountered(my_input, (3, 1))
    trees_encountered_5_1 = count_trees_encountered(my_input, (5, 1))
    trees_encountered_7_1 = count_trees_encountered(my_input, (7, 1))
    trees_encountered_1_2 = count_trees_encountered(my_input, (1, 2))
    product = trees_encountered_1_1 * trees_encountered_3_1 * trees_encountered_5_1 * trees_encountered_7_1 * trees_encountered_1_2
    print("Part two product: {}".format(product))

def count_trees_encountered(my_input, slope):
    trees_encountered = 0
    x = 0
    y = 0
    x_len, y_len = get_limiting_length(my_input)
    while y < y_len:
        character = my_input[y][x]
        is_tree = check_if_tree(character)
        if is_tree:
            trees_encountered = trees_encountered + 1
        x, y = traverse((x, y), slope)
        x = x % x_len
    return trees_encountered

def traverse(coordinates, slope):
    x = coordinates[0]
    y = coordinates[1]
    x = x + slope[0]
    y = y + slope[1]
    return (x, y)

def check_if_tree(character):
    if character == "#":
        return True
    else:
        return False

def get_limiting_length(my_input):
    x_len = len(my_input[0])
    y_len = len(my_input)
    return (x_len, y_len)

if __name__ == "__main__":
    main()