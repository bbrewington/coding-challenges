from pytest import mark
from day_04 import scan_letter_grid, read_input

input_example1 = """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
""".splitlines()[1:]

# (0, 5, horiz_lr), (1,4,horiz_rl), 
input_ex2_temp = """
.....SS...
.....AAA..
.....M.MM.
.....X..XX
..........
""".splitlines()[1:]

input_ex2_temp2 = """
...SXXMAS.
.SAMXMSMSA
.MXSXMAAMM
.SAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

input_example2 = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".splitlines()[1:]

input_ex2_masked = """
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
""".splitlines()[1:]

# {(0, 4, 'DIAG_UL_BR'),
#  (0, 5, 'HORIZ_LR'),
#  (1, 1, 'HORIZ_RL'),
#  (1, 6, 'VERT_DU'),
#  (2, 3, 'DIAG_BR_UL'), #note, this is actually DIAG_BL_UR
#  (3, 9, 'VERT_UD'),
#  (4, 0, 'HORIZ_LR'),
#  (4, 3, 'HORIZ_RL'),
 (6, 0, 'DIAG_BR_UL'),
 (6, 2, 'DIAG_BR_UL'),
 (6, 6, 'DIAG_BR_UL'),
 (6, 9, 'VERT_DU'),
 (9, 5, 'HORIZ_LR')}

def test_ex2_masked_same():
    scanned_reg = scan_letter_grid(input_example2)
    scanned_masked = scan_letter_grid(input_ex2_masked)
    assert scanned_reg == scanned_masked

@mark.parametrize("match_item", [
    (0, 4, "DIAG_UL_BR"),
    (0, 5, "HORIZ_LR"),
    (1, 1, "HORIZ_RL"),
    (1, 6, "VERT_DU")
])
def test_example2_temp(match_item):
    scanned = scan_letter_grid(input_ex2_masked)
    assert match_item in scanned
    assert len([x for x in scanned if x[0] == 0]) == 2
    # assert (0, 4, "DIAG_UL_BR") in scanned
    # assert len(scanned) == 18 #{
        # ()
        # (0, 5, "HORIZ_LR"),
        # (1, 1, "HORIZ_RL"),
        # (4, 3, 'HORIZ_RL'),
        # (4, 0, 'HORIZ_LR'),
        # (1, 6, 'VERT_DU'),
        # (0, 4, 'DIAG_UL_BR')
    # }

@mark.parametrize("letter_grid, matches_expected", [(
    input_example1, {
        (1, 1, 'VERT_DU'),
        (3, 0, 'HORIZ_LR'),
        (1, 1, 'HORIZ_RL'),
        (0, 2, 'DIAG_UL_BR')
    }
)])
def test_example1(letter_grid, matches_expected):
    assert scan_letter_grid(letter_grid) == matches_expected

def test_example2():
    scanned = scan_letter_grid(input_example2)
    assert len(scanned) == 18
