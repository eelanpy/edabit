# 74_return_index_capital:
import test
import string

def return_index_upper(str):
    lst_index = []
    for i,j in enumerate(str):
        if j in 'aeiou':
            lst_index.append(i)
    print(lst_index)

return_index_upper("Celebration")