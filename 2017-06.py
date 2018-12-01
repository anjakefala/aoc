def read_puzzle_input(loc='2017-06.txt'):
    return open(loc).readline()

def redistribute(banks_str):
    banks_arr = [int(bank) for bank in banks_str.split()]
    # first instance of the largest memory bank
    i = banks_arr.index(max(banks_arr))
    memory = banks_arr[i]
    banks_arr[i] = 0
    i += 1
    while memory:
        if i + 1 > len(banks_arr):
            i = 0
        banks_arr[i] += 1
        # move to the next memory bank
        i += 1
        memory -= 1
    return ' '.join([str(bank) for bank in banks_arr])


def steps_in_loop(first_state):
    seen_states = list()
    current_state = first_state
    while current_state not in seen_states:
        seen_states.append(current_state)
        new_state = redistribute(current_state)
        current_state = new_state
    return len(seen_states) - seen_states.index(current_state)

print(steps_in_loop(read_puzzle_input()))
