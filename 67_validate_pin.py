# 67_validate_pin:

def validate_pin(pin):
    valid_or_not = ''
    pin_str = str(pin)
    if type(pin) == int:
       valid_or_not = "True Valid"
    if len(pin_str) <= 6:
        valid_or_not = "True Valid"
    else:
        valid_or_not = "False valid"
    
    print(valid_or_not)

validate_pin(123)
    