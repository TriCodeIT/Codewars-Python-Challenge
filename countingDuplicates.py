#CODEWARS CHALLENGE

#Counting Duplicates

#Count the number of Duplicates
#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


def duplicate_count(text):
    dict = {i: text.count(i) for i in set(text.lower())}
    count = 0
    for i in dict.values():
        if i > 1:
            count += 1
    return count


print(duplicate_count('abcde'))
print(duplicate_count('aabbcde'))
print(duplicate_count('indivisibility'))
print(duplicate_count('Indivisibilities'))
