def is_palindrome(word):
    return word.lower() == word.lower()[::-1]

print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False
