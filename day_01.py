import sys


def at_index(items, i):
    return items[i % len(items)]


def solve_puzzle(input):
    matched = [int(digit) for i, digit in enumerate(input) if digit == at_index(input, i+1)]
    return sum(matched)


if __name__ == '__main__':
    result = solve_puzzle(sys.argv[1])
    print(result)
