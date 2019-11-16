
# def question_one():
#     """asls a true or false question"""
#     response = int(input("Alaska was the last state to enter the Union, true or false? Please enter 1 for True or 0 for False"))
#     correct_answer = 1
#     if response == correct_answer:
#         print("got it")
#         return 1
#     elif response != correct_answer:
#         print("wrong answer")
#         return 0

# total_score = 0
# result = question_one()
# total_score += result
# print(total_score)

def multiple_choice():
    queation_one = print("1.What is the a rough estimate of the population of New York City? Please enter a character a-e")
    answer_options = input(" a) 1 million\n b) 3 million\n c) 5 million\n d) 8 million\n e)10 million")
    correct_answer = "d"
    if answer_options.lower() == correct_answer:
        print ("Correct!")
    elif answer_options.lower() != correct_answer:
        print("Incorrect!")


multiple_choice()