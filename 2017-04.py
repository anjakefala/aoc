def read_puzzle_input(input_loc):
    passphrase_list = [phrase.rstrip() for phrase in open(input_loc).readlines()]
    return passphrase_list

def is_passphrase_valid(passphrase):
    words = set()
    passphrase = passphrase.split(' ')
    for word in passphrase:
        word = ''.join(sorted(word))
        if word in words:
            return False
        else:
            words.add(word)
    return True

def number_of_valid_passphrases(passphrase_list):
    return len([passphrase for passphrase in passphrase_list if is_passphrase_valid(passphrase)])



print(is_passphrase_valid('oaoe rxeq vssdqtu xrk cjv yaoqp loo'))
print(is_passphrase_valid('hello i am anja'))
print(is_passphrase_valid('hello i am i'))
print(number_of_valid_passphrases(read_puzzle_input('2017-04.txt')))

'''
--- Part Two ---

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

    abcde fghij is a valid passphrase.
    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
    iiii oiii ooii oooi oooo is valid.
    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

Under this new system policy, how many passphrases are valid?
'''
