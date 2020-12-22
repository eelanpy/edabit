# 72_flip_booleans:

def flip(arg):
    if arg == 0:
        return "boolean expected"
    elif arg == True:
        return False
    elif arg == False:
        return True
    else:
        return "boolean expected"

print(flip(234))
