# 37_calculate_tax:

def calculate_tax(original_price,city,time):
    dict1 = {
            'Chico': 50,
            'Groucho': 70,
            'Harpo': 50,
            'Zeppo': 40
            }
    calculation = original_price + original_price * 100 / dict1[city]  * 24 / time
    print("${}".format(calculation))

calculate_tax(300,'Harpo',5)
calculate_tax(400,'Harpo',6)
calculate_tax(500,'Harpo',7)
calculate_tax(600,'Harpo',8)



