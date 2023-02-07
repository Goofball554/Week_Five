def one_to_five(message):
    valid_input = False
    answer = int(input(message))
    count = 1
    
    while not valid_input and count < 3:
        if answer >= 1 and answer <= 5:
            valid_input = True
            count = 1

        else:
            answer = int(input('Please enter a number between 1 and 5, you entered an invalid number: '))
            count = count + 1

        if count == 3:
            print("You have entered the wrong thing 3 times, your system is locked.")
    return answer

response = one_to_five('Enter a number between 1 and 5: ')


if response >= 1 and response <= 5:
    print("Wonderful, thank you.")