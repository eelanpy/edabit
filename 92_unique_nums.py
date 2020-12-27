# 92_unique_nums:

def unique_nums(nums):
    dict_num = {}
    uni_num = []
    for i in nums:
        if i not in dict_num:
            dict_num[i] = 1
        elif i in dict_num:
            dict_num[i] += 1
    for i in dict_num.keys():
        if dict_num[i] == 1:
            uni_num.append(i)
    return uni_num
    print(uni_num)
    
print(unique_nums([1, 9, 8, 8, 7, 6, 1, 6]))
assert unique_nums([1, 9, 8, 8, 7, 6, 1, 6]) == [9, 7]

print(unique_nums([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]))
assert unique_nums([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) == [2, 1]

print(unique_nums([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))
assert unique_nums([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) == [5, 6]
            
    