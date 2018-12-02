def read_puzzle_input():
    return [word.rstrip() for word in open('2018-02.txt').readlines()]

def count_letters(words):
    '''
    count the number of words with exactly two and three letters
    '''
    box_counts = {2: 0, 3: 0}
    for word in words:
        word_count = {}
        for char in word:
            if char in word_count:
                word_count[char] += 1
            else:
                word_count[char] = 1
        if 2 in word_count.values():
            box_counts[2] += 1
        if 3 in word_count.values():
            box_counts[3] += 1
    return box_counts

def checksum(box_counts):
    return box_counts[2] * box_counts[3]


print(checksum(count_letters(read_puzzle_input())))
