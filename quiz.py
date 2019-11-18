questions = ["1.What is the a rough estimate of the population of New York City? Please enter a character between a-e.",
             "\n2.Who taught History of Mafic? Please enter a letter base on options below.",
             "\n3.How many states are there in the United States? Please enter an integer?",
             "\n4.How old was Voldemort when he opened the chanber of Secrets? Please enter an integer.",
             "\n5.Alaska was the last state to enter the union, true or false? Please enter 1 for True or 0 for False.",
             "\n6.Thestrals can only be seen by people who have witnessed death. enter 1 for True or 0 for False."]

answer_choices = [" a) 1 million\n b) 3 million\n c) 5 million\n d) 8 million\n e)10 million\n your answer:",
                " a) Professor\n b) Professor Lupin\n c) Professor McGonagall\n d) Professor Binns\n e) Professor Flitwick\n your answer:",
                "Enter an integer\nyour answer:",
                "Enter an integer\nyour answer:",
                "Enter 1 for True, 0 for false\nyour answer:",
                "Enter 1 for True, 0 for false\nyour answer:"]

correct_choices = ["d","8 million",
                   "d","professor Binns",
                   "50",
                   "16",
                   "0", "false",
                   "1", "true"]

answers = ["rough estimate of the population of New York City is 8 million",
           "Professor Binns taught history of Mafic",
           "There are 50 states in the United States",
           'False, Hawaii was the last state to enter the union',
           "The answer is True",
           "The answer is False"]

def quiz():
    score = 0
    check_answers = []
    
    for question,choices,correct_choice,answer in zip (questions,answer_choices,correct_choices,answers):
        print(question)
        user_answer = input(choices).lower()
        if user_answer in correct_choice:
            print("Correct")
            index = questions.index(question) +1
            check_answers.append(f" {index} correct")
            score += 1
        else:
            print("Incorrect", answer)      
            index = questions.index(question) +1
            check_answers.append(f" {index} Incorrect")  
    print("     Correctly answered",score, "out of", len(questions), "that is", round(score / len(questions),2) * 100, "%")
    print(check_answers)
    if score <= 3:
        print("You didn't do well")
    elif score == 5:
        print("You meet the passing line")
    elif score == 6:
        print("you are a genius!")
    
        

quiz()
