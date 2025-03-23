#Counting Words: Count the number of words in a sentence using a while loop.
def count_word(sentence):
    word_count = 0
    in_word = False
    i = 0
    
    while i < len(sentence):
        if sentence[i].isspace():
            in_word = False
        elif not in_word:
            in_word = True
            word_count += 1
        i += 1
    return word_count
sentence = "This is a sample sentence to count the words in the given sentence"
print(count_word(sentence))