# 59_nicknames_length:

def nicknames_len(names):
    """
    Input is a list 
    """
    dict_nicknames = {}
    for i in names:
        dict_nicknames[i.capitalize()] = len(i)
    print(dict_nicknames)
    for i in dict_nicknames.keys():
        print("{}, your nickname is: {}{}.".format(i,i[0],dict_nicknames[i]))



