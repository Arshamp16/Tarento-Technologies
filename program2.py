# Accept a String input
# Print the count of words in the String. Space is assumed to be the separator between words
# Print all numbers that are present in the String and also if they are odd or even. Numbers which are together should be counted as one number.

#It is a python 3 program


import re
import string
inp=str(input())
even,odd=[],[] #2 lists, one to store odd numbers and the other to store even numbers
digits=re.findall('\d+', inp) #find all digits
words= re.findall('\w+', inp) #find all words
for i in digits:
    even.append(int(i)) if int(i)%2==0 else odd.append(int(i)) #appending numbers in appropriate lists
print("Total words - ",len(words))
print("Odd numbers - ",*odd)
print("Even numbers - ",*even)


