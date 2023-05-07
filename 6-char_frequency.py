def character_frequency(string):

    string=string.lower().split()
    sample_dictionary={}
    
    for word in string:
        words=len(word)
        if words in sample_dictionary:
            sample_dictionary[words].add(word)
        else:
            sample_dictionary[words] = {word}
    print(sample_dictionary)
    return sample_dictionary

character_frequency("The way you see people is the way you treat them and the Way you treat them is what they become")
if character_frequency=="_main_":
    character_frequency