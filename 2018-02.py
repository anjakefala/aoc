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

def compare(word_a, word_b):
    for i in range(len(word_a)):
        subset_a = word_a[:i] + word_a[i+1:]
        subset_b = word_b[:i] + word_b[i+1:]
        if subset_a == subset_b:
            return (True, i)
    return (False, -1)

def find_fabric(boxes):
    for i in range(len(boxes)):
        current_box = boxes[i]
        for j in range(i+1, len(boxes)):
            second_box = boxes[j]
            have_fabric, k = compare(current_box, second_box)
            if have_fabric:
                return (i, j, k)


def checksum(box_counts):
    return box_counts[2] * box_counts[3]


print(checksum(count_letters(read_puzzle_input())))
boxes = read_puzzle_input()
i, j, k = find_fabric(boxes)
print(boxes[i][:k] + boxes[i][k+1:])
