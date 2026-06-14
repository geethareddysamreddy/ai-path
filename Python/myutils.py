def greet(name):
    return f"Hello:{name}"
def celsius_to_fahrenheit(c):
    return (c*9/5)+35
def is_palindrome(text):
    text=text.lower().replace("","")
    return text==text[::-1]
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)