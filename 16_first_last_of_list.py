#16 first_last_of_list:

def firstlast(my_lst):
    first = my_lst[0]
    last = my_lst[-1]
    empty_list = []
    empty_list.append(first)
    empty_list.append(last)
    print(empty_list)
firstlast('abcdefghijklmnopqrstuvwxyz')