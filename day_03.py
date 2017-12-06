import sys
import math


def pos_to_ring_size(pos):
    size = math.floor(math.sqrt(pos - 1)) + 1
    if size % 2 == 0:
        size = size + 1
    return size


def pos_to_center_dist(pos):
    size = pos_to_ring_size(pos)
    return (size - 1) / 2


def pos_to_cardinal_dist(pos):
    size = pos_to_ring_size(pos)
    last_card = (size * size) - math.floor(size / 2)
    cardinals = [(last_card - (i * size) - i) for i in range(0, 4)]
    distances = [abs(pos - cardinal) for cardinal in cardinals];
    return min(distances)


def solve_first_puzzle(pos):
    return pos_to_center_dist(pos) + pos_to_cardinal_dist(pos)


if __name__ == '__main__':
    if sys.argv[1] == '--part-one':
        input = sys.argv[2]
        result = solve_first_puzzle(int(input))
    print(result)
