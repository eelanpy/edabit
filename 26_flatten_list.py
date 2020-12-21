# 26_flatten_a_list:

def flatten(lists):
    lst = []
    for i in lists:
        for j in i:
            lst.append(j)
    print(lst)

flatten([[1,2], [3,4]])