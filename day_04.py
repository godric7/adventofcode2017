import sys
import functools

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]


def word_to_prime(word):
    factors = [PRIMES[ord(char) - ord('a')] for char in word]
    return functools.reduce(lambda x, y: x*y, factors, 1)


def is_passphrase_valid2(passphrase):
    words = [word_to_prime(word) for word in passphrase.split(' ')]
    if len(set(words)) == len(words):
        return True
    return False


def solve_second_puzzle(lines):
    return sum([1 for line in lines if is_passphrase_valid2(line.strip())])


def is_passphrase_valid(passphrase):
    words = passphrase.split(' ')
    if len(set(words)) == len(words):
        return True
    return False


def solve_first_puzzle(lines):
    return sum([1 for line in lines if is_passphrase_valid(line.strip())])


if __name__ == '__main__':
    if sys.argv[1] == '--part-one':
        input = sys.stdin.readlines()
        result = solve_first_puzzle(input)
    if sys.argv[1] == '--part-two':
        input = sys.stdin.readlines()
        result = solve_second_puzzle(input)
    print(result)
