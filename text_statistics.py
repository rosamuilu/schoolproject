source_text = "ASDF is the sequence of letters that appear on the first four keys on the home row of a QWERTY or QWERTZ keyboard. They are often used as a sample or test case or as random, meaningless nonsense. It is also a common learning tool for keyboard classes, since all four keys are located on Home row."

#number of letters
def number_of_letters_in(text):
    count = 0
    for character in text:
        if character.isalpha():
            count += 1
    
    return count

print(number_of_letters_in(source_text))

#number of words
def number_of_words_in(text):
    words = str.split(text)
    count = len(words)
    return count
    

print(number_of_words_in(source_text))

#number of sentences
def number_of_sentences_in(text):
    count = 0
    for character in text:
        if character == ".":
            count += 1
    
    return count

print(number_of_sentences_in(source_text))

#average word length
def average_word_length(text):
    words = str.split(text)
    length = []

    for x in words:
        count = 0
        for character in x:
            if character.isalpha():
                count += 1
        
        length.append(count)
    
    print(length)
    average = sum(length) / len(length)
    return average

print(average_word_length(source_text))