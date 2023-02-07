def one_to_five(message):
    valid_input = False
    answer = input(message)
    count = 1
    
    while not valid_input:
        if answer == "abc":
            valid_input = True
            count = 1

        else:
            answer = input('Please enter the password, what you entered is incorrect: ')
            count = count + 1

        if count == 3:
            print("You have entered the wrong thing 3 times, your system is locked.")
    return answer

response = one_to_five('Enter the password: ')


if response == "abc":
    print("Wonderful, thank you.")