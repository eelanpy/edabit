#38_transform_values:

def transform_values(dict1):
    new_dict = {}
    for i in dict1.keys():
        new_dict[i] = dict1[i] * dict1[i]
    
    print(new_dict)


transform_values({'a':1, 'b':2,'c':3})