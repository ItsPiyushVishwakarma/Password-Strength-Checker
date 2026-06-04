def check_password_strength(password):

    #initialize flags for password requirements
    has_upper = False
    has_lower = False                       #flags to check different 
    has_digit = False                       #requirements
    has_special = False
    
    missing = []
    score = 0

    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    # Check each character
    for char in password:
                                            
        if char.isupper():                  #Loop through each character in the password and check if it meets the requirements
            has_upper = True                # and set flags

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True
    
    #Length check
    if len(password) >= 8:
        score += 20
    else:
        missing.append("Minimum 8 characters")

    #Uppercase check
    if has_upper:
        score += 20
    else:
        missing.append("uppercase letter")

    #Lowercase check
    if has_lower:
        score += 20
    else:
        missing.append("lowercase letter")

    #Number check
    if has_digit:
        score += 20
    else:
        missing.append("Number")
    
    #Special Character check
    if has_special:
        score += 20
    else:
        missing.append("Special Character")

    # Detwermine password strength
    if score == 100:
        strength = "Strong Password"
    
    elif score >= 60:
        strength = "Moderate Password"
   
    else:
        strength = "Weak Password"

    return strength, score, missing
    

#User Input
password = input("Enter a password: ")

result,score,missing = check_password_strength(password)

#Create strength bar
filled = score // 5
bar = "█" * filled + "-" * (20 - filled)

#output
print("\nPassword Strength: ",result)
print("[" + bar + "] ",score,"%")

#Show missing requirements
if missing:
    print("\nMissing Requirements: ")
    for item in missing:
        print("- " + item)