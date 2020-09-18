#CODEWARS CHALLENGE

#Duplicate Encoder

#The goal of this exercise is to convert a string to a new string where each character 
#in the new string is "(" if that character appears only once in the original string, 
#or ")" if that character appears more than once in the original string. 
#Ignore capitalization when determining if a character is a duplicate.

# Examples

# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

def duplicate_encode(word):
    #your code here 
    word = list(map(lambda x: x.lower(), word))

    unique = set(word)

    unique_counts = {}

    for elem in unique:
        unique_counts[elem] = word.count(elem)

    output = ""
    for elem in word:
        if unique_counts[elem] < 2:
            output += '('
        else:
            output += ')'

    return output
    

print(duplicate_encode("babibubebo"))
print(duplicate_encode("aiueo"))
print(duplicate_encode("bbbbb"))

print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))


