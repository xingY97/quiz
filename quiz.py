
def quiz_questions():
    score = 0
    multiple_choice_1 = print("1.What is the a rough estimate of the population of New York City? Please enter a character between a-e.")
    answer_options_1 = input(" a) 1 million\n b) 3 million\n c) 5 million\n d) 8 million\n e)10 million")
    correct_answer_1 = "d"
    if answer_options_1.lower() == correct_answer_1:
        print ("Correct!")
        score += 1
    elif answer_options_1.lower() != correct_answer_1:
        print("Incorrect, the answer is 'd) 8 million!'")
        

    multiple_choice_2 = print("\n2.Who taught History of Mafic? Please enter a letter base on option.")
    answer_options_2 = input(" a) Professor\n b) Professor Lupin\n c) Professor McGonagall\n d) Professor Binns\n e) Professor Flitwick")
    correct_answer_2 = "d"
    if answer_options_2.lower() == correct_answer_2:
        print ("Correct!")
        score += 1
    elif answer_options_2.lower() != correct_answer_2:
        print("Incorrect, the answer is 'd) Professor McGonagall!'")

    #numeric 
    numeric_response_1 = int(input("\n3.How many states are there in the United States? Please enter an integer?"))
    numeric_response_answer_1 = 50
    if numeric_response_1 == numeric_response_answer_1:
        print("Correct!")
        score += 1
    elif numeric_response_1 > numeric_response_answer_1:
        print ("The number you entered is too large, the correct answer is 50")
        
    elif numeric_response_1 < numeric_response_answer_1:
        print ("The number you entered is too small, the correct answer is 50")
        

    numeric_response_2 = int(input("\n4.How old was Voldemort when he opened the chanber of Secrets? Please enter an integer."))
    numeric_response_answer_2 = 16
    if numeric_response_2 == numeric_response_answer_2:
        print("Correct!")
        score += 1
    elif numeric_response_2 > numeric_response_answer_2:
        print ("The number you entered is too large, the correct answer is 16")
        
    elif numeric_response_2 < numeric_response_answer_2:
        print ("The number you entered is too small, the correct answer is 16")

    #Boolean

    Boolean_1 = int(input("\n5.Alaska was the last state to enter the union, true or false? Please enter 1 for True or 0 for False."))
    Boolean_answer_1 = 0
    if Boolean_1 == Boolean_answer_1:
        print ("Good job, the answer is False, Hawaii was the last state to enter the Union")
        score += 1
    elif Boolean_1 != Boolean_answer_1:
        print("You are wrong, Hawaii was the last state to enter the Union")
        

    Boolean_2 = int(input("\n6.Thestrals can only be seen by people who have witnessed death. enter 1 for True or 0 for False."))
    Boolean_answer_2 = 1
    if Boolean_2 == Boolean_answer_2:
        print ("Correct! The answer is True.")
        score += 1
    elif Boolean_2 != Boolean_answer_2:
        print("Incorrect! The answer if True, Thestrals can only be seen by people who have witnessed death.")
        
    print(f"Each question worth 1 point, this is your score {score}")
#def numeric_response():
#def True_False_question():

        




quiz_questions()
#numeric_response()
#True_False_question()