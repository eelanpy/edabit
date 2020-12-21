#28_flip_a_dict:

def flip_dict(dict):
    new_dict = {v:k for k,v in dict.items()}
    return new_dict
print(flip_dict({'a':1,'b':2,'c':3}))