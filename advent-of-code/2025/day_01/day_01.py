from typing import List, Tuple

def read_input(file: str) -> List[str]:
    list1 = []
    with open(file, 'r') as f:
        file_contents = f.readlines()
        for line in file_contents:
            list1.append(line.strip())
    return list1

def parse_instruction(instruction):
    direction = -1 if instruction.startswith("L") else 1
    instruction_amt = int(instruction[1:])
    return direction, instruction_amt

def count_zero_crossings(start_pos, instruction, count_mode):
    direction, instruction_amt = parse_instruction(instruction)
    range_end = start_pos + (direction * instruction_amt) + direction
    dial_values = [x % 100 for x in range(start_pos, range_end, direction)]
    if dial_values[0] == 0:
        dial_values.pop(0)
    
    if count_mode == "part1":
        return_value = int(dial_values[-1] == 0)
        return return_value
    elif count_mode == "part2":
        return_value = dial_values.count(0)
        return return_value
    else:
        raise ValueError("count_mode must be one of 'part1' or 'part2'")

def rotate_dial(start_pos: int, instruction: str, count_mode: str) -> Tuple[int, int]:
    # print(f"initial_pos={start_position}")
    # print(f"{direction=}")
    direction, instruction_amt = parse_instruction(instruction)
    final_pos_raw = start_pos + direction * instruction_amt
    # print(f"{final_pos_raw=}")
    final_pos = final_pos_raw % 100
    # print(f"{final_pos=}")
    num_pass_zero = count_zero_crossings(start_pos, instruction, count_mode)
    # print(f"{num_pass_zero=}")
    return final_pos, num_pass_zero

def day_01_part1(input_file: str) -> int:
    num_zeros = 0
    input_list = read_input(input_file)
    pos = 50
    for i, instr in enumerate(input_list):
        # print(f"{i=}, {instr=}, initial_pos={pos}", end=", ")
        pos, _ = rotate_dial(pos, instr, count_mode="part1")
        # print(f"final_pos={pos}")
        if pos == 0:
            num_zeros += 1
    return num_zeros

def day_01_part2(input_file: str) -> int:
    final_num_pass_zero = 0
    input_list = read_input(input_file)
    pos = 50
    for _, instr in enumerate(input_list):
        # print(f"{i=}, {instr=}, initial_pos={pos}", end=", ")
        pos, num_pass_zero = rotate_dial(pos, instr, count_mode="part2")
        # print(f"final_pos={pos}, num_pass_zero={num_pass_zero}")
        final_num_pass_zero += abs(num_pass_zero)
    print(f"{final_num_pass_zero=}")
    return final_num_pass_zero
