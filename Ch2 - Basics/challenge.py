# Palindrome - Reads a string the same way
# Characters = strings, numbers - No puctuations or spaces
# 1. Merge the entire string (Remove any puctiations, spaces)
# 2. Take input like exit from user and quit
# 3. Reverse the merged string and compare with merged screen
# 4. If same = palindrome else false
import re

def merge_character(testchar):
    new_alphanum = re.sub('[^A-Za-z0-9]+', '', testchar)
    return new_alphanum
def inverse_alphanum(testchar):
    new_inverse = merge_character(testchar)[::-1]
    return new_inverse

testchar = input("Enter a string to test for palindrome or \'exit\': ")
lower_testchar = testchar.lower()
if lower_testchar == "exit":
    print("Bye")
elif merge_character(lower_testchar) == inverse_alphanum(lower_testchar):
    print("Palindrone Test: True")
else:
    print("Palindrone Test: Failed")
