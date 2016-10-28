

class Hangman(object):

    
    def __init__(self,word):
        self.word = word
        
        self.guessed = []
        self.correct = []
        self.current = ['_']*len(word)

    def is_in(self, guess):

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


    def is_done(self):
        if '_' not in self.current:
            return True
        else:
            return False

    def set_guess(self, guess):
        ind = 0
        while ind != -1:
            if ind == 0:
                ind = self.word.find(guess, ind)

            else:
                ind = self.word.find(guess, ind+1)
            if ind != -1:
                self.current[ind] = guess
            if ind == 0:
                ind = 1
        
        
            
        

    def __repr__(self):
        current = ''
        for i in self.current:
            current = current + '{0} '.format(i)
        return current



def main():
    word = raw_input('Please give me a word: ')
    hang = Hangman(word)
    while True:
        print hang
        print ''
        guess = raw_input('Guess a letter: ')
        hang.is_in(guess)
        if hang.is_done():
            print "You won!!"
            break

        
    

if __name__ == '__main__':

    main()

##    x = 'hello'
##    y = ['h','e','l','l','o']
##    u = x.find('l')
##    z = x.find('l',u + 1)
##    hh = x.find('l', z +1)
##    print '{0}  {1}   {2}'.format(u, z, hh)

    
        
        
