# 34_passwd_to_csv.py:
def passwd_to_csv(read_file,write_file):
    lst = []
    with open(read_file, 'r'):
        for i in read_file:
            lst.append(i)
    with open(read_file, 'w'):
        print('lst[0][0]      lst[0]')