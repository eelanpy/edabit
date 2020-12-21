# 19_Summing anything:

def sum_any(data):
    counter = 0
    data_type = type(data)
    
    if data_type in (list,tuple):
        for item in data:
            counter += item
    elif data_type in (int,float):
        counter += data
    else:
	print("Sorry, we can not add your numbers!")
    print(counter)
sum_any([1.0,2.0,3,4.0])



def sum_any2(data2):
    counter = 0
    data_type = type(data2)

    try:
        for item in data2:
            counter += item
    except:
        counter += data2
    print(counter)

sum_any2(1)  
