'''def password_strength(password):
    if len(password) < 8:
        print("password must be at least 8 characters.")
    if not any(char.isupper() for char in password):
        print("Weak: Must include an uppercase letter.")
    if not any(char.islower() for char in password):
        print("Weak: Must include a lowercase letter.")
    if not any(char.isdigit() for char in password):
        print("Weak: Must include a number.")
    if not any(char in "!@#$%^&*()_+" for char in password):
        print("Weak: Must include a special character.")
    print("password is strong")

def main():
    password = input("Enter a password: ")
    password_strength(password)

main()'''
def upper_case(password):
    cnt=0
    for char in password:
        if char.isupper():
            cnt+=1
    if cnt<=0:
        print("password is weak , must include a upper case character")
        return 0
    else:
        return 1
    
def lower_case(password):
    cnt=0
    for char in password:
        if char.islower():
            cnt+=1
    if cnt<=0:
        print("password is weak , must include a lower case character")
        return 0
    else:
        return 1
def digits(password):
    cnt=0
    digits="0123456789"
    for char in password:
        if char in digits:
            cnt+=1
    if cnt<=0:
        print("password is weak , must include a digit")
        return 0
    else:
        return 1
def special_character(password):
    cnt=0
    characters="!@#$%^&*()_+"
    for char in password:
        if char in characters:
            cnt+=1
    if cnt<=0:
        print("password is weak , must include a digit")
        return 0
    else:
        return 1
def main():
    password=input("enter a password: ")
    if len(password)<8:
        print("password is weak, password must include 8 characters")
    else:    
        cnt1=upper_case(password)
        cnt2=lower_case(password)
        cnt3=digits(password)
        cnt4=special_character(password)
        if cnt1+cnt2+cnt3+cnt4==4:
            print("password is strong")
main()