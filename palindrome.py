
def isPalindrome(string: str):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString

isPalindrome('abcdcba')