#21_tuple_records:

def tuple_records(list_of_tuples):
    empty_lst = []
    for tple in list_of_tuples:
        for j in tple:
            empty_lst.append(j)
    for i in range(len(empty_lst)):
        print("\n")
        print(empty_lst[i])
        i += 1
tuple_records([('Donald', 'Trump', 7.85),
('Vladimir', 'Putin', 3.626),
('Jinping', 'Xi', 10.603)])