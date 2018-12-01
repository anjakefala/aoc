def read_puzzle_input(input_loc='2017-05.txt'):
    return [int(jump.rstrip()) for jump in open(input_loc).readlines()]

def steps_to_exit(jump_instructions):
    exit = False
    i = 0
    total_steps = 0
    while not exit:
        total_steps += 1
        num_jumps = jump_instructions[i]
        if num_jumps + i > len(jump_instructions)-1 or num_jumps + i < 0:
            return total_steps
        else:
            if num_jumps >= 3:
                jump_instructions[i] = num_jumps - 1
            else:
                jump_instructions[i] = num_jumps + 1
            i = num_jumps + i




print(steps_to_exit(read_puzzle_input()))


