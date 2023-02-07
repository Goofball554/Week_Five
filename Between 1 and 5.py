def one_to_five(message):
    valid_input = False
    answer = int(input(message))
    
    while not valid_input:
        if answer >= 1 and answer <= 5:
            valid_input = True
        else:
            answer = int(input('Please enter a number between 1 and 5, you entered an invalid number: '))
    return answer

response = one_to_five('Enter a number between 1 and 5: ')


if response >= 1 and response <= 5:
    print("Wonderful, thank you.")