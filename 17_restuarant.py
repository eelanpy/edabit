#17_restaurant:

def restuarant(dict1):
    money = 0
    for _ in dict1.values():
        if dict1['order'] == 'sandwich':
            
            money += 10
            print("We have sandwich and it costs 10 dollars and your total is {}.".format(money))
        elif dict1['order'] == 'elephant':
                print("We don't have elephant today and your total is ${}".format(money))
        

restuarant({'order':'sandwich'})