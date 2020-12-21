#07_printing_multiplication_for_list_of_numbers:

def some_tables(lst):
    for i in lst:
        print("This is {} times table:".format(i))
        print("-------------------------- \t")
        for j in range(1,13):
            
            print("{} x {} = {} ".format(i, j, i*j))
        print('\n')
        print('\t')
input_lst = [i for i in range(1,13)]
some_tables(input_lst)