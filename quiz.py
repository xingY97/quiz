
def multiple_choice():
    question_one = print("1.What is the a rough estimate of the population of New York City? Please enter a character a-e")
    answer_options = input(" a) 1 million\n b) 3 million\n c) 5 million\n d) 8 million\n e)10 million")
    correct_answer = "d"
    if answer_options.lower() == correct_answer:
        print ("Correct!")
    elif answer_options.lower() != correct_answer:
        print("Incorrect, the answer is d) 8 million!")

def numeric_response():
    question_two = int(input("How many states are there in the United States? Please enter an integer?"))
    correct_answer = 50
    if question_two == correct_answer:
        print("Correct!")
    elif question_two > correct_answer:
        print ("The number you entered is too large, the correct answer is 50")
    elif question_two < correct_answer:
        print ("The number you entered is too small, the correct answer is 50")

def True_False_question():
    


multiple_choice()
numeric_response()