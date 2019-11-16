# Are You a Fan Quiz?

## Description
In this project we will write a Python program to create a quiz on a topic of your choosing!

Credit to Gina Sprint for [this project](https://www.engage-csedu.org/find-resources/are-you-fan-quiz) posted on EngageCSEdu

## Learning Outcomes
By completing this project, you should be able to…

1. Implement functions and call functions
1. Implement lists
1. Implement loops
1. Implement conditionals
1. String manipulation and formatting
1. Make connections to fields outside of CS
1. Get input from the user and display output

## Requirements

Your quiz must contain at least 5 questions. These 5 questions include at least 2 of each of the following
different types of questions:

### Multiple choice (5 options a-e)
The user enters in a character "a" through "e" for their answer.

Example:

1) What is the a rough estimate of the population of New York City? Please enter
a character a-e.

a) 1 million

b) 3 million

c) 5 million

d) 8 million

e) 10 million

Note: The answer is d) 8 million!

### Numeric Response
The user enters in a numeric response to an open ended question. I recommend prompting the user to enter
an integer. If you choose to use floats, be specific to the user about how they should enter their response (i.e.
rounded and/or a certain number of decimal places).

Example:

How many states are there in the United States? Please enter an integer.

Note: The answer is 50!

### True/False (Boolean)
The user enters 1 or 0 in response to a true or false statement. Compare the response to the correct answer and return a 1 if they got it right and a 0 if not. 

Example:

Alaska was the last state to enter the Union, true or false? Please enter 1 for
True or 0 for False.

Note: The answer is False! Hawaii was the last state to enter the Union.

### Additional requirements:
1. For each question:

    1. Define a function. The function should return the following:

    1. 1 (int) if the user answered correctly

    1. 0 (int) if the user answered incorrectly

    1. Explicitly tell the user the format in which they should enter their response.

    1. Number each question.

Check the user's answer for correctness using an if­else structure. If the user answers
correctly, inform the user. Otherwise, provide the correct answer to the user.

2. Keep track of the  the number of correct answers (this is the user's quiz score).

3. Keep track of the correct and incorrect answers in a list.

4. At the end of the quiz, tell the user their final score, which questions were correct or incorrect, plus a fun statement about how much of a "fan"
they are of the quiz's topic (use an if­elif­else structure, which means you need at least 3
different fun statements based on the user's score).

### Stretch Requirements/Challenges (Optional)
1. Modify your program to be able to handle incorrect input from the user, such as a character besides a-e being entered in a multiple choice question
1. Modify your program to include a menu that lets the user take the quiz multiple times 
1. Modify your program to inlcude a menu that lets the user choose from a set of multiple quizzes to take
