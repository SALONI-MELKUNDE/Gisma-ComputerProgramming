
passwords = input("Enter a list of passwords, separated by commas: ").split(",")

for password in passwords:
    password = password.strip() 
    
    
    if len(password) < 8:
        print("Weak password: too short")
        continue

    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    if has_upper and has_lower and has_digit:
        print("Strong password!")
        break  
    else:
        
        print("Moderate password: missing character types")

