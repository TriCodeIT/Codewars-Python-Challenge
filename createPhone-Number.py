#CODEWARS CHALLENGE

#Create Phone Number
#Write a function that accepts an array of 10 integers (between 0 and 9), 
#that returns a string of those numbers in the form of a phone number.

def create_phone_number(n):
    #your code here 
    phone_number = '('
    for i, num in enumerate(n):
        if i < 3:
            phone_number += str(num)
            if i == 2:
                phone_number += ') '
        elif i <= 13:
            phone_number += str(num)
            if i == 5:
                phone_number += '-'
    return phone_number
