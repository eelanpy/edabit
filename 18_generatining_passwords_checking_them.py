#18_generatining_passwords_checking_them
import string
import random
def checking_password():
    while True:
        letter = ''
        letter_lower = random.choice(string.ascii_lowercase)
        letter_upper = random.choice(string.ascii_uppercase)
        letter = letter_lower + letter_upper
        list_symbols = ['!','#','$','%','&','(',')','*','+',',','-','.','/',':',';'] 
        rand_symbols = random.choice(list_symbols)
        letter += rand_symbols
        print("Your password is {}".format(letter))
        input_password = input(str("What is the password?  "))
        if input_password != letter:
            print("Your password is incorrect")
        else:
            print("Your password is correct!")
            break
checking_password()