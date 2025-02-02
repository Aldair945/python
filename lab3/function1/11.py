def palindrome(phrase):
    phrase = phrase.replace(" ","").lower()
    palindrome = phrase[::-1]
    if phrase == palindrome:
        return True
    return False
phrase = input()
print(palindrome(phrase))