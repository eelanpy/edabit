#13_printing_tuple_records:

import pandas as pd

def tuple_records(lst):
    lst_tuple = tuple(lst)
    lst_tple_dict = {}
    for _ in lst_tuple:
        lst_tple_dict['first_name'] = lst_tuple[0]
        lst_tple_dict['last_name'] = lst_tuple[1]
        lst_tple_dict['dpa'] = lst_tuple[2]
    
    print(lst_tple_dict)
tuple_records(('Donald','Trump',0.8))