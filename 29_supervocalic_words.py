#29_supervocalic_words:

def get_sv(wrd):
    dict1 = {'a':0,'e':0,'i':0,'o':0,'u':0}
    lst = []
    for i in wrd:
        lst.append(i)
    for i in lst:
        if i in dict1.keys():
            dict1[i] += 1
    




    print(dict1)

get_sv('yeaheauuuiou')