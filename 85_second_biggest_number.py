# 85_second_biggest_number:

def second_largest(list1):
    nums = []
    for i,j in enumerate(list1):
                nums.append(j)
    nums2 = [i for i in sorted(nums)]
    print(nums2[-2])
    
second_largest([54, 23, 11, 17, 10])
second_largest([10, 40, 30, 20, 50])

second_largest([25, 143, 89, 13, 105])