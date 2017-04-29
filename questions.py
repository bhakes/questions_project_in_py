## This program implements a simple fill-in the blank Intro to Programming Quiz
## in a command-line interface. The program has 3 difficulty settings.
## These difficulty settings are easy/medium/hard.
## Once the users selects their desired difficulty level, they are given a series
## of 4 - 5 questions from the Intro to Programming subject material.
## These questions are loaded from a CSV file.

## import csv library
import csv
difficulty_list = ['Easy','Medium','Hard']

def load_questions(csv_file):
    """ Loads questions from previously prepared .csv file """

    ## gets csv file with questions and puts it into a list question_list
    with open(csv_file, 'r') as questions:
        reader = csv.reader(questions, delimiter='\t')
        question_list = list(reader)

    ## data cleaning, eliminate csv header
    question_list = question_list[1:]

    ## more data cleaning, select only first 3 columns
    index = 0
    while index < len(question_list):
        holding_str = question_list[index][0].split(',')
        holding_str = holding_str[:3]
        question_list[index] = holding_str
        index += 1

    return question_list

## get user difficulty
def get_user_difficulty():
    """ prompt user for difficulty level and continue requesting until
     proper response is received """
    user_input = raw_input("What level of difficulty? (Easy/Medium/Hard)\n")
    while user_input not in difficulty_list:
        user_input = raw_input("Please choose either Easy, Medium, or Hard (case sensitive).\n")
    print "Difficulty level set to: " + user_input + "."
    return user_input


def ask_question_and_check_response(question_from_questions, correct_answer):
    """ get user answer to fill in the blank question """

    ## prompt user for answer based on the Question
    user_input = raw_input(question_from_questions + " (case sensitive)\n")

    ## check for correct answer
    ## if not correct, prompt user
    while user_input != correct_answer:
        user_input = raw_input("Incorrect. Please try again\n")

    ## update question string to remove blanks and insert correct answer
    updated_string = question_from_questions.replace('____',correct_answer)

    ## if correct, return congratulations to user and repeat question & answer
    return "That's correct! " + updated_string

def play_game():
    """Main game play thread"""

    ## get difficulty and questions
    difficulty = get_user_difficulty()
    questions = load_questions("questions.csv")

    ## select and print all questions that are of the user inputed
    ## difficulty level
    index = 0
    while index < len(questions):
        if questions[index][0] == difficulty:
            print ask_question_and_check_response(questions[index][1], questions[index][2])
        index += 1

    ## Congratulate user
    print "Congratulations, you've answered all of the " + difficulty +" questions correctly!"

    ## see if user wants to play again
    user_input = raw_input("Would you like to try again? (Y/N)\n")
    if user_input.upper() == 'Y':
        return play_game()
    else:
        return "Okay, have a nice day!"

print play_game()
