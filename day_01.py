import sys


def at_next(items, i):
    return items[(i + 1) % len(items)]


def solve_puzzle(input):
    matched = [int(digit) for i, digit in enumerate(input) if digit == at_next(input, i)]
    return sum(matched)


def at_halfway(items, i):
    half = int(len(items) / 2)
    return items[(i + half) % len(items)]


def solve_second_puzzle(input):
    matched = [int(digit) for i, digit in enumerate(input) if digit == at_halfway(input, i)]
    return sum(matched)


if __name__ == '__main__':
    if sys.argv[1] == '--part-two':
        result = solve_second_puzzle(sys.argv[2])
    else:
        result = solve_puzzle(sys.argv[1])
    print(result)
