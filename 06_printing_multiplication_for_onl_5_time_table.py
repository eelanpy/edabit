#06_printing_multiplication for only 5 time table:

def times_table(j):
    for i in range(1,13):
        print('{} x {}  = {}'.format(j,i,j*i))

times_table(5)
    