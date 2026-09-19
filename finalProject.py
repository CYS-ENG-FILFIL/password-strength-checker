import re
def main():
    password=input("Enter your password : ")
    print(checkPassword(password))
def checkLength(password):
    if len(password)>7:
        return True
    else:
        return False
def checkNum(password):
    for char in password:
        if char.isdigit():
            return True
    return False
def checkUppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False
def checkSpecialChar(password):
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
def checkPassword(password):
    score = 0
    if checkLength(password):
        score += 1
    if checkNum(password):
        score += 1
    if checkUppercase(password):
        score += 1
    if (password):
        score += 1

    if score == 4:
        return "Very Strong"
    elif score == 3:
        return "Strong"
    elif score == 2:
        return "Medium"
    else:
        return "Weak"
if __name__ == "__main__":
    main()