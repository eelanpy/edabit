# 94_square_dict:

def square_dict(num):
    dict1 = {}
    for i in range(1,num+1):
        dict1[i] = i * i
    return dict1

print(square_dict(8))

assert square_dict(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}