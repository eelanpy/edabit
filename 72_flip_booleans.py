# 72_flip_booleans:

def flip(arg):
    """
    My function will put the opposite of the boolean value. Example if I put False it will 
    return True. Another example is that python thinks 0 is False but we want 
    it to return 
    """
    if arg == 0:
        return "boolean expected"
    elif arg == True:
        return False
    elif arg == False:
        return True
    else:
        return "boolean expected"

print(flip(234))
