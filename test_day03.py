from day_03 import pos_to_cardinal_dist, pos_to_center_dist, solve_first_puzzle


def test_should_find_distance_to_center():
  assert pos_to_center_dist(1) == 0
  assert pos_to_center_dist(2) == 1
  assert pos_to_center_dist(11) == 2
  assert pos_to_center_dist(28) == 3
  assert pos_to_center_dist(9) == 1
  assert pos_to_center_dist(10) == 2


def pos_to_cardinal_dist():
  assert pos_to_cardinal_dist(1) == 0
  assert pos_to_cardinal_dist(11) == 0
  assert pos_to_cardinal_dist(28) == 0
  assert pos_to_cardinal_dist(9) == 1
  assert pos_to_cardinal_dist(10) == 1
  assert pos_to_cardinal_dist(32) == 2
  assert pos_to_cardinal_dist(36) == 2

def test_should_solve_first_puzzle_for_the_provided_exemples():
  assert solve_first_puzzle(12) == 3
  assert solve_first_puzzle(23) == 2
  assert solve_first_puzzle(1024) == 31
