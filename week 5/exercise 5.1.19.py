# 2

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter in "OQ":
        print(letter+"u"+suffix)
    else:
        print(letter + suffix)

# 3


def count_letters(word, character):
    count = 0
    for letter in word:
        if letter == character:
            count +=1
    return(count)


count_letters("banana", "a")

