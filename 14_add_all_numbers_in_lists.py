#14_add_all_numbers_in_lists:
def add_all(lst):
    counter = 0
    for i in lst:
        counter += i
    return counter
print(add_all([1,2,3,4,5,6,7,8]))
assert add_all([1,2,3,4,5,6,7,8]) == 36