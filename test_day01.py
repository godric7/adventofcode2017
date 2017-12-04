from day_01 import solve_puzzle


def test_solve_correctly_the_povided_examples():
    assert solve_puzzle('1122') == 3
    assert solve_puzzle('1111') == 4
    assert solve_puzzle('1234') == 0
    assert solve_puzzle('91212129') == 9
