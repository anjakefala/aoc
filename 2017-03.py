def solve_1(num):

    def which_shell(num):
        '''
        first output: the shell in which the number is located
        second output: the dimensions of the array
        this is the lowerbound of the steps
        can we get the dimensions for that shell?
        '''
        shell = 0
        i = 0
        current_shell_limit = 1
        while not shell:
            i += 1
            current_shell_limit += i*8
            if num <= current_shell_limit:
                shell = i
        return (shell, shell*2+1)

    return which_shell(num)



'''
# First Square (3x3; 8 numbers) 2*4
# Second Square (5x5; 16 numbers) 4*4
# Third Square (7x7; 24 numbers) 6*4
'''


print("12: ")
print(solve_1(12))
print("---------")
print("23: ")
print(solve_1(23))
print("---------")
print("1024: ")
print(solve_1(1024))
print("---------")
print("289326: ")
print(solve_1(289326))
