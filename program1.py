#Given a paragraph count the frequency of vowels and consonants in each word and capitalize the vowels/consonants in each word whose frequency is the highest. If the frequency of vowels and consonants are equal then capitalize the whole word.
#it is a python 3 program
    
s = input().split()
for word in s :
    vowels = consonants = 0
    word.lower()
    for letter in word :
        if letter in ('a','e','i','o','u') : vowels += 1
        elif 'a' <= letter <= 'z' : consonants += 1
    if vowels == consonants : print(word.upper(),end = "")
    elif vowels > consonants :
        for letter in word :
            if letter in ('a','e','i','o','u') : print(letter.upper(),end = "")
            elif 'a' <= letter <= 'z' : print(letter,end = "")
            else : print(letter,end = "")
    else :
        for letter in word :
            if letter in ('a','e','i','o','u') : print(letter,end = "")
            elif 'a' <= letter <= 'z' : print(letter.upper(),end = "")
            else : print(letter,end = "")
    print(end = " ")
