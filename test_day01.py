from day_01 import solve_puzzle, solve_second_puzzle


def test_solve_correctly_the_povided_examples():
    assert solve_puzzle('1122') == 3
    assert solve_puzzle('1111') == 4
    assert solve_puzzle('1234') == 0
    assert solve_puzzle('91212129') == 9


def test_part_two_solves_correctly_the_povided_examples():
    assert solve_second_puzzle('1212') == 6
    assert solve_second_puzzle('1221') == 0
    assert solve_second_puzzle('123425') == 4
    assert solve_second_puzzle('123123') == 12
    assert solve_second_puzzle('12131415') == 4
