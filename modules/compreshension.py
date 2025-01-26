def binary(digits):
    digits = digits[::-1]
    value = 0
    for i in range(len(digits)):
        value += value + int(digits[i]) * 2**i
        
        return value
    