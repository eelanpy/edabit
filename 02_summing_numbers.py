#02_summing_numbers:

def sum_nums(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(sum_nums(15,7,25))
