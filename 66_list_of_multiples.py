# 66_list_of_multiples:

def lst_of_multipules(table, range_num):
    lst = []
    for i in range(1,range_num+1):
        lst.append(i * table)

    print('List of {} time table up to {}: {}\n'.format(table,range_num,lst))

lst_of_multipules(7,10)
lst_of_multipules(8,11)
lst_of_multipules(9,12)
lst_of_multipules(10,13)
