#!/Users/bin/python3

import random
"""
Quiz game throwing random questions at the user, continue the game if user choses and
display score at the end
"""

questionset = {
    'Which animal lives in the North pole? : ': 'polar bear',
    'Which is the largest animal? : ': 'elephant',
    'Which is the fastest land animal?  ': 'cheetah'
}
score = 0
questions = list(questionset.keys())


def get_random_question():
    # TODO: delete seleted question from the list
    randomquestion = random.choice(questions)
    return randomquestion


def getanswer(question):
    return questionset[question]


def display_result():
    if score != 0:
        print("\n\nCongratulations! Your score is : ", score)
    else:
        print("\n\nYou got Duck! :) ")


if __name__ == "__main__":
    print("Welcome to Quiz session!")

    choice = 'y'

    while(choice.lower() == 'y'):

        randomq = get_random_question()
        answer = getanswer(randomq)

        ans = input(randomq)
        ans = ans.lower()  # answers are stored in lower case
        print(ans)

        if ans == answer:
            print("correct")
            score = score+1
        else:
            print("wrong!")

        choice = input(
            "Do you like to continue with the next question?(y/n) : ")

    display_result()
