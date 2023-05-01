def n_letter_dictionary(my_string):

    my_string=my_string.lower().split()
    sample_dictionary={}
    
    for word in my_string:
        words=len(word)
        if words in sample_dictionary:
            sample_dictionary[words].add(word)
        else:
            sample_dictionary[words] = {word}
    print(sample_dictionary)
    return sample_dictionary

n_letter_dictionary("The way you see people is the way you treat them and the Way you treat them is what they become")