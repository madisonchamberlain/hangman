def noose():
    return str(' |')

def head():
    return str(' 0')

def torso():
    return str(' |')


def torso_left_arm():
    return str('/|')


def torso_both_arms():
    return str('/|\\')


def left_leg():
    return str('/')

def both_legs():
    return str('/ \\')


    #phases:
def phase_zero():
    print()
    print(noose())
    return

def phase_one():
    print()
    print(noose())
    print(head())
    return

def phase_two():
    print()
    print(noose())
    print(head())
    print(torso())
    return

def phase_three():
    print()
    print(noose())
    print (head())
    print(torso_left_arm())
    return

def phase_four ():
    print()
    print(noose())
    print(head())
    print(torso_both_arms())
    return

def phase_five():
    print()
    print(noose())
    print(head())
    print(torso_both_arms())
    print(left_leg())
    return

def phase_six():
    print()
    print(noose())
    print(head())
    print(torso_both_arms())
    print(both_legs())
    return



def man_phases(wrong_guess):

    if wrong_guess == 1:
        phase_zero()

    elif wrong_guess == 2 :
        phase_one()

    elif wrong_guess == 3:
        phase_two()

    elif wrong_guess == 4:
        phase_three()

    elif wrong_guess == 5:
        phase_four()

    elif wrong_guess == 6:
        phase_five()

    elif wrong_guess == 7:
        phase_six()
    return

####need valid input

def game_over(reason,secret_word):
#guessed string
    if reason == 'win':
        print('You correctly guessed the secret word:', secret_word, end = '')
        return False
#man dies
    elif reason == 'death':
        print('You failed to guess the secret word:', secret_word, end = '')
        return False



def get_secret_word():
    secret_word = str(input('Please enter a word to be guessedthat does not contain ? or white space: '))
    while (len(secret_word) == 0) or ' ' in secret_word or '?' in secret_word :
        secret_word = str(input('Please enter a word to be guessedthat does not contain ? or white space: '))
   # while ' ' in secret_word:
    #    secret_word = str(input('Please enter a word do be guessed that does not contain ? or white space: '))
    #while '?' in secret_word:
     #   secret_word = str(input('Please enter a word do be guessed that does not contain ? or white space: '))

    new_lines = str('\n')*30
    print(new_lines)
    return secret_word




def my_input(input):
    input = input.strip(' ')
    if input  == '':
        print('You must enter a guess.')
        get_guess()
    if len(input) > 1:
        print('You can only guess a single character.')
        get_guess()
   # if input in guesses:
    #    print('You already guessed the letter: ', guess)
     #   get_guess()

    return input


def get_guess():
    guess = str(my_input(input('Please enter your next guess: ')))
    return guess

def guessing_process(secret_word, guess, wrong_guess, guess_string):

   # print (guess_string)
    ###add array
    checker = False
    index = 0
    playing = 1

    for pos, letter in enumerate(secret_word):
        guess_list = list(guess_string)  ########################replace
        secret_word = list(secret_word)
        if guess ==  letter:
            guess_list[pos] = letter
            checker = True


        guess_string = ''.join(guess_list)
        secret_word = ''.join(secret_word)
        #index += 1

    if guess_string == secret_word:
        game_over('win',secret_word)
        guess_string = ""
        playing = 0

    if checker == False:

        wrong_guess = wrong_guess + 1
        #man_phases(wrong_guess)
        if wrong_guess >= 7:
            game_over('death',secret_word)
            guess_string = ""
            playing = 0
    man_phases(wrong_guess)
    print(guess_string)
    answer = [guess_string, wrong_guess, playing]
    return answer

def game():
    guesses = []
    secret_word = get_secret_word()
    wrong_guess = 0
    guess_string = '?' * len(secret_word)
    print(guess_string)
    print("So far you have guessed:", str(guesses).replace("[", "").replace("]", "").replace("'", "").replace("'", ""))
    guess = get_guess()
    guesses.append(guess)
    guesses.sort()
    ans = guessing_process(secret_word,guess, wrong_guess, guess_string)
    print ("So far you have guessed:", str(guesses).replace("[", "").replace("]", "").replace("'", "").replace("'", ""))
    wrong_guess = ans[1]
    guess_string = ans[0]
    playing = ans[2]

    while True:

        guess = get_guess()
        length = len(guess)
        if guess in guesses:
            print('You already guessed the letter: ', guess)
            guess = get_guess()
            length = len(guess)
        if (guess not in guesses) and (length == 1) and (guess != ""):
            guesses.append(guess)
        guesses.sort()
        ans = guessing_process(secret_word, guess, wrong_guess, guess_string)
        playing = ans[2]
        if playing == 0:
            break
        if playing:
            wrong_guess = ans[1]
            guess_string = ans[0]
            print("So far you have guessed:",str(guesses).replace("[", "").replace("]", "").replace("'", "").replace("'", ""))




game()
