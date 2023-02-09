s = input("Please input a password: ")

def checkLength(s):
    if len(s) > 10 and len(s) < 20:
       checkChar(s)
    
    else: 
        print("You have not entered a valid password.")

def checkChar(s):
    Special = "()[],.:;!@#$%^&*"
    yesSpecial = " "
    for eachChar in s:
        if eachChar in Special:
            yesSpecial = yesSpecial + eachChar
    
    if yesSpecial != " ":
        checkNum(s)

    else: 
        print("You have not entered a valid password.")


def checkNum(s):
    Number = "1234567890"
    yesNumber = " "
    for eachChar in s:
        if eachChar in Number:
            yesNumber = yesNumber + eachChar
    
    if yesNumber != " ":
        print("You have entered a valid password")


    else: 
        print("You have not entered a valid password.")

print(checkLength(s))