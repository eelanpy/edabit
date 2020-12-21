# 63_where_is_bob:

def find_bob(list_n):
    joined_n = " ".join(list_n)
    if 'bob' in joined_n or 'Bob' in joined_n:
        print(joined_n.find('bob'))

find_bob(["Jimmy",'Layla','Bob'])