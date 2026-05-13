import re
import random
import string

common_passwords = ["123456", "password", "qwerty", "abc123"]

def check_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1

    # Numbers
    if re.search(r"\d", password):
        score += 1

    # Special Characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1

    # Common Password Check
    if password.lower() in common_passwords:
        return "Very Weak"

    # Final Result
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"

def suggest_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

password = input("Enter Password: ")

strength = check_strength(password)

print("\nPassword Strength:", strength)

if strength != "Strong":
    print("Suggested Strong Password:", suggest_password())