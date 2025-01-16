def plusOne(digits):
    counter = 0
    reversed_digits = digits[::-1]
    for i in reversed_digits:
        i = i + 1
        reversed_digits[counter] = i
        if i == 10 and counter == (len(digits) - 1):
            reversed_digits[counter] = 0
            reversed_digits[:0] = [1]
            return reversed_digits
        elif i == 10:
            reversed_digits[counter] = 0 
            counter = counter + 1
        else:
            return reversed_digits[::-1]
    return reversed_digits[::-1]