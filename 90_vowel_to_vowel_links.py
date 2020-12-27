# 90_vowel_to_vowel_links:
def vowel_links(txt):
    return txt[0] in 'aieou' and txt[-1] in 'aeiou'
        
    
assert vowel_links("a very large appliance") == True

assert vowel_links("go to edabit") == False

assert vowel_links("an open fire") == True

assert vowel_links("a sudden applause") == True
