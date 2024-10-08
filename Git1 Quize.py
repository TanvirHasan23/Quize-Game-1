# ---------------------------------------------------------
questions = {
    'Who created Python?: ': 'A',
    'What year wass Python Created?: ': 'B',
    'Python is tributed to which comedy group?: ': 'C',
    'Is the Earth round?: ': 'A'
}

options = [['A. Guido van Rossum', 'B. Elon Musk', 'C. Bill Gates', 'D. Mark Zuckerburg'],
           ['A. 1989', 'B. 1991', 'C. 2000', 'D. 2016'],
           ['A. Lonely Island', 'B. Smosh', 'C. Monty Python', 'D. SNL'],
           ['A. True', 'B. False', 'C. Sometimes', 'D. What is Earth?']]


def new_game():
    guesses = []  # Q1: What?
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('---------------------------------------------------------')
        print(key)
        for i in options[question_num - 1]:  # Q2: What?Why?
            print(i)
        guess = input('Enter (A, B, C or D): ')
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print('CORRECT!')
        return 1  # Q3: What the use of it?
    else:
        print('WRONG! ')
        return 0


# ---------------------------------------------------------

def display_score(correct_guesses, guesses):
    print('---------------------------------------------------------')
    print('RESULT')
    print('---------------------------------------------------------')

    print('Answers: ', end='')  # Q6: end = '' uses

    for i in questions:
        print(questions.get(i), end='')  # Q5: What? Why?
    print()

    print('Guesses: ', end='')
    for i in guesses:
        print(i, end='')
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print('Your Score is: ' + str(score) + '%')


# ---------------------------------------------------------

def play_again():
    response = input('Do you want to play again? ( yes or no): ')
    response = response.upper()

    if response == 'YES':
        return True
    else:
        return False


# ---------------------------------------------------------
new_game()

while play_again():  # Q6: How
    new_game()

print('Bye!')

## Main problem is display_score section
## Analyse the new_game section