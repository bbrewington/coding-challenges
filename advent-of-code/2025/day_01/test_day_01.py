from pytest import mark

from day_01 import read_input, rotate_dial, day_01_part1, day_01_part2, count_zero_crossings

def test_read_input():
    example_input = read_input("input_example.txt")
    assert example_input[0] == "L68", "Error: first value"
    assert example_input[-1] == "L82", "Error: last value"

@mark.parametrize("start_position, instruction, expected_result", [
    (50, "L68", 82),
    (82, "L30", 52),
    (52, "R48", 0),
    (0, "L5", 95),
    (95, "R60", 55),
    (55, "L55", 0),
    (0, "L1", 99),
    (99, "L99", 0),
    (0, "R14", 14),
    (14, "L82", 32)
])
def test_rotate_dial(start_position: int, instruction: str, expected_result: int):
    assert rotate_dial(start_position, instruction, count_mode="part1")[0] == expected_result

def test_day01_part1():
    assert day_01_part1("input_example.txt") == 3

def test_part2_example():
    pos = 50
    pos, num_pass_zero = rotate_dial(pos, "R1000", count_mode="part2")
    assert num_pass_zero == 10

def test_rotate_dial_custom():
    final_pos, num_pass_zero = rotate_dial(0, "L5", count_mode="part1")
    assert final_pos == 95
    assert num_pass_zero == 0

@mark.parametrize("start_pos, instruction, end_pos, num_ones", [
    (50, 'R8', 58, 0),
    (58, 'R28', 86, 0),
    (86, 'R43', 29, 1),
    (29, 'L29', 0, 1),
    (0, 'L3', 97, 0),
    (97, 'R29', 26, 1),
    (26, 'L24', 2, 0),
    (2, 'L12', 90, 1),
    (90, 'R22', 12, 1),
    (12, 'R5', 17, 0),
    (17, 'L5', 12, 0),
    (12, 'R43', 55, 0)
])
def test_rotate_part2(start_pos, instruction, end_pos, num_ones):
    end_pos_calc, num_pass_zero = rotate_dial(start_pos, instruction, count_mode="part2")
    assert end_pos_calc == end_pos
    assert num_pass_zero == num_ones

@mark.parametrize("start_position, instruction, num_cross_zero", [
    (50, "L68", 1),
    (82, "L30", 0),
    (52, "R48", 1),
    (0, "L5", 0),
    (95, "R60", 1),
    (55, "L55", 1),
    (0, "L1", 0),
    (99, "L99", 1),
    (0, "R14", 0),
    (14, "L82", 1)
])
def test_count_zero_crossings(start_position: int, instruction: str, num_cross_zero: int):
    assert count_zero_crossings(start_position, instruction, count_mode="part2") == num_cross_zero

def test_day01_part2():
    assert day_01_part2("input_example.txt") == 6
