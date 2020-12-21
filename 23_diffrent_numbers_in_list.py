#23_how_many_different_numbers:

def diff_num(lst):
    dict1 = {}
    for i in lst:
        dict1[i] = 1
        if dict1[i] in dict1:
            dict1[i] += 1

    return len(dict1)


def diff_num1(lst):
    list1 = []
    for i in lst:
       if i not in list1:
           list1.append(i)
    return len(list1)

def diff_num2(lst):
    return len(set(lst))

print(diff_num([1,2,3,1,2,3,5]))
print(diff_num1([1,2,3,1,2,3,5]))
print(diff_num2([1,2,3,1,2,3,5]))