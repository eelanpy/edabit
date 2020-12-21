# 25_sum_numbers:

def sum_num(lst):
    total = 0
    for item in lst:
        if type(item) == int:
            total += item
    return total

print(sum_num([1,2,[4],34,'abcefghijklmnopqrstuwxyz']))


def sum_num1(lst):
    return sum([i for i in lst if type(i) == int])

print(sum_num1([1,2,4,34,'abcefghijklmnopqrstuwxyz']))
