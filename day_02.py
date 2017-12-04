import sys


def line_checksum(line):
    values = [int(token) for token in line.split()]
    return max(values) - min(values)


def solve_puzzle(lines):
    return sum([line_checksum(line.strip()) for line in lines])


if __name__ == '__main__':
    if sys.argv[1] == '--part-one':
        input = sys.stdin.readlines()
        result = solve_puzzle(input)
    print(result)
