s = input("Please input a password: ")
valid = False

def checkChar(s):
    Special = "()[],.:;!@#$%^&*"
    yesSpecial = " "
    for eachChar in s:
        if eachChar in Special:
            yesSpecial = yesSpecial + eachChar
    
    if yesSpecial != " ":
        print("You have entered a valid password")

    else: 
        print("You have not entered a valid password.")

    return yesSpecial



print(checkChar(s))
