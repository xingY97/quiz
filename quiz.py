
def multiple_choice():
    question_one = print("1.What is the a rough estimate of the population of New York City? Please enter a character between a-e.")
    answer_options = input(" a) 1 million\n b) 3 million\n c) 5 million\n d) 8 million\n e)10 million")
    correct_answer = "d"
    if answer_options.lower() == correct_answer:
        print ("Correct!")
    elif answer_options.lower() != correct_answer:
        print("Incorrect, the answer is d) 8 million!")

def numeric_response():
    question_two = int(input("\n2.How many states are there in the United States? Please enter an integer?"))
    correct_answer = 50
    if question_two == correct_answer:
        print("Correct!")
    elif question_two > correct_answer:
        print ("The number you entered is too large, the correct answer is 50")
    elif question_two < correct_answer:
        print ("The number you entered is too small, the correct answer is 50")

def True_False_question():
    question_three = int(input("\n3.Alaska was the last state to enter the union, true or false? Please enter 1 for True or 0 for False."))
    correct_answer = 0
    if question_three == correct_answer:
        print ("Good job, the answer is False, Hawaii was the last state to enter the Union")
    elif question_three != correct_answer:
        print("You are wrong, Hawaii was the last state to enter the Union")



multiple_choice()
numeric_response()
True_False_question()