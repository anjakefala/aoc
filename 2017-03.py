def solve_1(num):

    def which_shell(num):
        '''
        first output: the shell in which the number is located
        second output: the dimensions of the array
        this is the lowerbound of the steps
        '''
        shell = 0
        i = 0
        current_shell_max = 1
        while not shell:
            i += 1
            current_shell_max += i*8
            if num <= current_shell_max:
                shell = i
        return (shell, shell*2+1)

    shell, dim = which_shell(num)
    # first output: coordinates of the first point in the shell of dimension dim x dim
    first_elem_coor = (dim, 1)
    first_elem_val = (dim-2) * (dim-2) + 1
    distance = num - first_elem_val

    # 0 - right
    # 1 - top
    # 2 - left
    # 3 - bottom
    # which side of the square our assigned point is
    side = (distance) // (dim-1)

    # calculate the coordinates of our point
    if side == 0:
    # correct
        num_coor = (first_elem_coor[0], distance + first_elem_coor[0])
    elif side == 1:
    # correct
        num_coor = (distance+1-(dim-1), dim-1)
    elif side == 2:
    # incorrect
        num_coor = (0, distance+1-(dim-1)*2)
    else:
    # correct
        num_coor = (distance-(dim-1)*2-(dim-2), 0)

    # manhattan distance
    print('num_coor: {0}'.format(num_coor))
    print('side: {0}'.format(side))
    return abs(dim//2 - num_coor[0]) + abs(dim//2 - num_coor[1])

def solve_2(num):
    '''
    What is the first value written that is *larger* than your puzzle input?
    '''


print(solve_1(289326))
