def captcha(seq_digits):
    sum = 0
    halfway = len(seq_digits)//2
    for i in range(len(seq_digits)):
        j = (i + halfway) % len(seq_digits)
        if seq_digits[i] == seq_digits[j]:
            sum += int(seq_digits[i])
    print(sum)

captcha('1212')
captcha('1221')
captcha('123123')
captcha('12131415')
