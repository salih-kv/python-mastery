def count_vowels_consonants(sentence):
    vowels = "aeiou"
    sentence = sentence.lower()
    vowels_count = sum(1 for char in sentence if char in vowels)
    consonants_count = sum(1 for char in sentence if char.isalpha() and char not in vowels)
    return vowels_count, consonants_count

vowels, consonants = count_vowels_consonants("Hello World!")
print(f"Vowels: {vowels}, Consonants: {consonants}")
