print('Please think of a number between 0 and 100!')

low = 0
high = 100
answer = (low + high)//2

while True:
    print('Is your secret number ' + str(answer) + '?')
    submission = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")
    if submission == 'c':
        break
    elif submission == 'h':
        high = answer
    elif submission == 'l':
        low = answer
    else:
        print('Sorry, I did not understand your input.')
    answer = (low + high)//2

print('Game over. Your secret number was: ' + str(answer))
    
