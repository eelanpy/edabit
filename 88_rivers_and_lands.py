# 88_rivers_and_lands:

def rivers_lands(list1):
    board  = {}
    for i in list1:
        if i == 1 and 'rivers' not in board:
            board['rivers'] = 1
        elif i == 1:
            board['rivers'] += 1
        elif i == 0 and 'lands' not in board:
            board['lands'] = 1
        else:
            board['lands'] += 1
        
    return board
            
    
def rivers_lands2(list1):
    board  = {}    
    board['rivers'] = sum(list1)
    board['lands'] = len(list1) - board['rivers']
    return board
    
print(rivers_lands2([1,0,1,0,1]))
# {'rivers':3, 'lands':2}