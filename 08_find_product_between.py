#08_find_product_between:

def find_prod_between(table,first,end):
    for i in range(first,end+1):
        if i % table == 0:
            print(i)
        
    
find_prod_between(5,13,100)