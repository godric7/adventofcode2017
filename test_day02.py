from day_02 import line_checksum, solve_puzzle


def test_should_compute_correctly_a_line_checksum():
    assert line_checksum('5 1 9 5') == 8
    assert line_checksum('7 5 3') == 4
    assert line_checksum('2 4 6 8') == 6


def test_should_solve_correctly_the_input_checksum():
    lines = [
      '5 1 9 5',
      '7 5 3',
      '2 4 6 8',
    ]
    assert solve_puzzle(lines) == 18
