

class Hangman(object):

    
    def __init__(self,word,num_wrong):
        self.word = word.upper()      
        self.guessed = []
        self.correct = []
        self.current = ['_']*len(word)
        self.number_can_get_wrong = int(num_wrong)
        self.count_wrong = 0


    def is_in(self, guess):
        '''
        Checks to see if the letter is in the word.
        '''
        if guess in self.guessed:
            print "You already guessed that"
        else:
            self.guessed.append(guess)

        if guess in self.word:
            self.correct.append(guess)
            self.set_guess(guess)
            print "That letter is in the word!!!"
        else:
            print "Sorry, that letter is not in the word"
            self.count_wrong += 1
                

    def is_done(self):
        '''
        Checks to see if all blanks are gone
        '''
        if '_' not in self.current:
            return True
        else:
            return False


    def set_guess(self, guess):
        '''
        This function sets the guess.
        '''
        ind = 0
        while ind != -1:
            ind = self.word.find(guess, ind)
            if ind != -1:
                self.current[ind] = guess   
                ind += 1
        
        
    def __repr__(self):
        current = ''
        for letter in self.current:
            current = current + '{0} '.format(letter)
        return current


def main():
    '''
    Main function that runs when you run this from command line
    '''
    word = raw_input('Please give me a word: ')
    wrong = raw_input('How many chances should the player get to make a mistake? ')
    hang = Hangman(word, wrong)
    while True:
        print hang
        print ''
        guess = raw_input('Guess a letter: ')
        hang.is_in(guess.upper())
        if hang.is_done():
            print "You won!!"
            break
        elif hang.count_wrong > hang.number_can_get_wrong:
            print "you lose"
            break


if __name__ == '__main__':
    main()


    
        
        
