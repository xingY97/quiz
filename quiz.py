
def multiple_choice():
    multiple_choice_1 = print("1.What is the a rough estimate of the population of New York City? Please enter a character between a-e.")
    answer_options_1 = input(" a) 1 million\n b) 3 million\n c) 5 million\n d) 8 million\n e)10 million")
    correct_answer_1 = "d"
    if answer_options_1.lower() == correct_answer_1:
        print ("Correct!")
    elif answer_options_1.lower() != correct_answer_1:
        print("Incorrect, the answer is 'd) 8 million!'")

    multiple_choice_2 = print("\n2.Who taught History of Mafic? Please enter a letter base on option.")
    answer_options_2 = input(" a) Professor\n b)Professor Lupin\n c) Professor McGonagall\n d) Professor Binns\n e) Professor Flitwick")
    correct_answer_2 = "d"
    if answer_options_2.lower() == correct_answer_2:
        print ("Correct!")
    elif answer_options_2.lower() != correct_answer_2:
        print("Incorrect, the answer is 'd) Professor McGonagall!'")
    

def numeric_response():
    numeric_response_1 = int(input("\n2.How many states are there in the United States? Please enter an integer?"))
    numeric_response_answer_1 = 50
    if numeric_response_1 == numeric_response_answer_1:
        print("Correct!")
    elif numeric_response_1 > numeric_response_answer_1:
        print ("The number you entered is too large, the correct answer is 50")
    elif numeric_response_1 < numeric_response_answer_1:
        print ("The number you entered is too small, the correct answer is 50")

def True_False_question():
    Boolean_1 = int(input("\n3.Alaska was the last state to enter the union, true or false? Please enter 1 for True or 0 for False."))
    Boolean_answer_1 = 0
    if Boolean_1 == Boolean_answer_1:
        print ("Good job, the answer is False, Hawaii was the last state to enter the Union")
    elif Boolean_1 != Boolean_answer_1:
        print("You are wrong, Hawaii was the last state to enter the Union")





multiple_choice()
numeric_response()
True_False_question()