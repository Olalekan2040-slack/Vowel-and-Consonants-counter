import string

def VowelConsonant_count(letters):
    total_vowel =0
    total_consonant =0
    for val in letters:
        if val in string.punctuation or val in string.digits or val ==" ":
            pass
        elif val.lower() in ["a","e","i","o","u"]:
            total_vowel+=1
        else:
            total_consonant +=1
    return (f'There are {total_vowel} vowels and {total_consonant} consonants in {letters}') 

    
letters = input("Input anu word(s) here: ")
print(VowelConsonant_count(letters))