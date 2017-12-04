import sys


def line_checksum(line):
    values = [int(token) for token in line.split()]
    return max(values) - min(values)


def solve_puzzle(lines):
    return sum([line_checksum(line.strip()) for line in lines])


def line_evenly_divisible_result(line):
    values = [int(token) for token in line.split()]
    for i in values:
        for j in values:
            if i > j and i % j == 0:
                return i / j


def solve_second_puzzle(lines):
    return sum([line_evenly_divisible_result(line.strip()) for line in lines])


if __name__ == '__main__':
    if sys.argv[1] == '--part-one':
        input = sys.stdin.readlines()
        result = solve_puzzle(input)
    if sys.argv[1] == '--part-two':
        input = sys.stdin.readlines()
        result = solve_second_puzzle(input)
    print(result)
