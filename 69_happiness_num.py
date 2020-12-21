# 69_happiness_num:

def happiness_num(emojis):
    counter_emoji = 0
    for emoji in emojis:
        if emoji == ":)":
            counter_emoji += 1
        if emoji == "(:":
            counter_emoji += 1
        if emoji == "):":
            counter_emoji -= 1
        if emoji == ":(":
            counter_emoji -= 1
    return counter_emoji

print(happiness_num([":)","(:","):"]))
    