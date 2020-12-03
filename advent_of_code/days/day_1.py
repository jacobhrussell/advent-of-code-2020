import csv

# https://adventofcode.com/2020/day/1
def main():

    my_input = []
    with open('advent_of_code/input/day_1.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            my_input.append(row[0])
    two_numbers = find_two_numbers(my_input)
    multiple = two_numbers[0] * two_numbers[1]
    print("{} + {} = 2020 and {} * {} = {}".format(
            two_numbers[0], 
            two_numbers[1], 
            two_numbers[0], 
            two_numbers[1], 
            multiple
        )
    )

    three_numbers = find_three_numbers(my_input)
    multiple = three_numbers[0] * three_numbers[1] * three_numbers[2]
    print(" {} + {} + {} = 2020 and {} * {} * {} = {}".format(
            three_numbers[0],
            three_numbers[1],
            three_numbers[2],
            three_numbers[0],
            three_numbers[1],
            three_numbers[2],
            multiple
        )
    )

def find_two_numbers(my_input):
    for i in range(len(my_input)):
        x = int(my_input[i])
        for j in range(len(my_input)):
            if i != j:
                if x + int(my_input[j]) == 2020:
                    return (x, int(my_input[j]))
            j = j + 1
        i = i + 1

def find_three_numbers(my_input):
    for i in range(len(my_input)):
        x = int(my_input[i])
        for j in range(len(my_input)):
            y = int(my_input[j])
            for k in range(len(my_input)):
                z = int(my_input[k])
                if x != y and y != z:
                    if x + y + z == 2020:
                        return [x, y, z]
                k = k + 1
            j = j + 1
        i = i + 1

if __name__ == "__main__":
    main()