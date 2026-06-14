import random
import string

def generate_password(length, digit, spl):
    special = "@_"
    
    
    first = random.choice(string.ascii_uppercase)
    chars = []

    
    if digit:
        chars.append(random.choice(string.digits))
    if spl:
        chars.append(random.choice(special))

    
    pool = string.ascii_letters
    if digit:
        pool += string.digits
    if spl:
        pool += special

    remaining_length = length - 1 - len(chars) 
    chars.extend(random.choices(pool, k=remaining_length))

    random.shuffle(chars)
    return first + "".join(chars)

def get_yes_no(prompt):
    while True:
        ans = input(prompt + " (y/n): ").strip().lower()
        if ans in ("y", "n"):
            return ans == "y"

def get_len():
    while True:
        try:                                    
            n = int(input("Enter password length (min 8): "))
            if n >= 8:
                return n
            else:
                print("Length must be at least 8.")
        except ValueError:
            print("Please enter a valid number.")



def main():
    length = get_len()
    digit = get_yes_no("Include digits?")
    spl = get_yes_no("Include special chars?")
    pwd = generate_password(length, digit, spl)
    print("Generated Password:", pwd)
    print("Done!")         

main()