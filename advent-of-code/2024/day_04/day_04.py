def read_input(filename):
    with open(filename, "r") as f:
        letter_grid = [x.strip() for x in f.readlines()]
    return letter_grid

def scan_horiz(letter_grid):
    matches = set()
    ncol = len(letter_grid[0])
    for i, row in enumerate(letter_grid):
        for j, _ in enumerate(row):
            if j >= ncol - 3:
                break
            if row[j:(j + 4)] == "XMAS":
                matches.add((i, j, "HORIZ_LR"))
            elif row[j:(j + 4)] == "SAMX":
                matches.add((i + 3, j, "HORIZ_RL"))
    return matches

def scan_vert(letter_grid):
    matches = set()
    ncol = len(letter_grid[0])
    nrow = len(letter_grid)
    for col_num in range(ncol):
        col = [row[col_num] for row in letter_grid]
        for row_num in range(nrow):
            if row_num >= nrow - 3:
                break
            col_subset = ''.join(col[row_num:(row_num + 4)])
            if col_subset == "XMAS":
                matches.add((row_num, col_num, "VERT_UD"))
            elif col_subset == "SAMX":
                matches.add((row_num, col_num + 3, "VERT_DU"))
    return matches

def scan_diag(letter_grid):
    nrow = len(letter_grid)
    ncol = len(letter_grid[0])
    
    # matches_ul_br: upper left to bottom right
    matches_ul_br = set()
    anchor_points_ul_br = [(x, y) for x in range(nrow - 3) for y in range(0, ncol - 3)]
    for anchor_point in anchor_points_ul_br:
        print(anchor_point, end=", ")
        row_num, col_num = anchor_point
        diag = ''.join([letter_grid[row_num + i][col_num + i] for i in range(4)])
        print(f"{row_num=}, {col_num=}, {diag=}, match: {diag in ('XMAS', 'SAMX')}")
        if diag == "XMAS":
            matches_ul_br.add((row_num, col_num, "DIAG_UL_BR"))
        if diag == "SAMX":
            matches_ul_br.add((row_num - 3, col_num - 3, "DIAG_BR_UL"))
    
    # matches_ur_bl: upper right to bottom left
    matches_ur_bl = set()
    anchor_points_ur_bl = [(x, y) for x in range(nrow - 3) for y in range(ncol - 3, ncol)]
    for anchor_point in anchor_points_ur_bl:
        row_num, col_num = anchor_point
        diag = [letter_grid[row_num + i][col_num - i] for i in range(4)]
        if diag == "XMAS":
            matches_ur_bl.add((row_num, col_num, "DIAG_UR_BL"))
        if diag == "SAMX":
            matches_ur_bl.add((row_num - 3, col_num + 3, "DIAG_BL_UR"))
    
    return matches_ul_br, matches_ur_bl

def scan_letter_grid(letter_grid):
    matches = set()
    matches = matches.union(scan_horiz(letter_grid))
    matches = matches.union(scan_vert(letter_grid))
    matches_ul_br, matches_ur_bl = scan_diag(letter_grid)
    matches = matches.union(matches_ul_br)
    matches = matches.union(matches_ur_bl)
    return {x for x in matches if x != []}

if __name__ == "__main__":
    letter_grid = read_input("input_example1.txt")
    print(scan_letter_grid(letter_grid))
