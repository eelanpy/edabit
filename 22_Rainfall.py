# 22_Rainfall:

def rain_fall():
    empty_dict = {}
    city_input = input("What city is having a rainfall? ")
    rain_fall_input = input("How much rain fall is in the city {}? ".format(city_input))
    if city_input:
        empty_dict[city_input] = rain_fall_input

    for i in empty_dict:
        print("{}:".format(i))
        print("{}".format(empty_dict[i]))
rain_fall()