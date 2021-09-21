import csv

# https://adventofcode.com/2020/day/5

def main():
    my_input = []
    with open('advent_of_code/input/day_3.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            my_input.append(row[0])

if __name__ == "__main__":
    main()