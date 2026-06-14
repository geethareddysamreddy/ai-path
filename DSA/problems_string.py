# ============ Problem 1 - Reverse String ============
def reverse_string(s):
    rev = ""
    for char in s:
        rev = char + rev
    return rev

# ============ Problem 2 - Check Palindrome ============
def is_palindrome(s):
    return s == reverse_string(s)

# ============ Problem 3 - Count Vowels & Consonants ============
def count_vowels_consonants(s):
    vowels = 0
    consonants = 0
    for char in s:
        if char in "aeiou":
            vowels += 1
        elif char != " ":
            consonants += 1
    return f"Vowels: {vowels}, Consonants: {consonants}"

# ============ Problem 4 - Check Anagram ============
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# ============ Problem 5 - Word Frequency ============
def word_frequency(s):
    d = {}
    for word in s.split():
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

# ============ Main ============
print(reverse_string("hello"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(count_vowels_consonants("hello world"))
print(is_anagram("listen", "silent"))
print(word_frequency("hello world hello python world hello"))