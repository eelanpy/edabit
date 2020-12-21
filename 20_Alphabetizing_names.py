# 20_Alphabetizing_names

def test1(list):
    d = {}
    for i in list:
        #print(i)
        key = i['last'] + ' ' + i['first']
        print(key)
        d[key] = i
    #print('\n')
    #print(d)
    sorted_keys = sorted(d.keys())

    new_list = []
    for i in sorted_keys:
        new_list.append(d[i])
    print(new_list)




people = [{'first':'Reuven', 'last':'Lerner',
'email':'reuven@lerner.co.il'},
{'first':'Donald', 'last':'Trump',
'email':'president@whitehouse.gov'},
{'first':'Donald', 'last':'Trump',
'email':'president@kremvax.ru'}
]

#test1(people)

import operator
def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts, key=operator.itemgetter('last', 'first'))

print(alphabetize_names(people))

