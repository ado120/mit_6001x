import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join(sorted(list(set(string.ascii_lowercase) - set(lettersGuessed))))


print(getAvailableLetters(lettersGuessed))