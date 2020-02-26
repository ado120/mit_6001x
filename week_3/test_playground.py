secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'l']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    test = [char in lettersGuessed for char in secretWord]
    return all(test)

print(isWordGuessed(secretWord, lettersGuessed))
print(isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))

# print(set(secretWord))
# print(set(lettersGuessed))
# print(set(secretWord) >= set(lettersGuessed))
# print(set(secretWord) & set(lettersGuessed))
# print(set(secretWord) <= set(lettersGuessed))