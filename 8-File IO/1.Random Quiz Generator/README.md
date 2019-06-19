# Random Quiz Generator

Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas, your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

Here is what the program does:
* Creates 35 different quizzes.
* Creates 50 multiple-choice questions for each quiz, in random order.
* Provides the correct answer and three random wrong answers for each question, in random order.
* Writes the quizzes to 35 text files.
* Writes the answer keys to 35 text files.

This means the code will need to do the following:

* Store the states and their capitals in a dictionary.
* Call open(), write(), and close() for the quiz and answer key text files.
* Use random.shuffle() to randomize the order of the questions and multiple-choice options.

After you run the program, this is how your capitals-quiz-1.txt file will look, though of course your questions and answer options may be different from those shown here, depending on the outcome of your random.shuffle() calls:

```
Name:

Date:

Period:

                    State Capitals Quiz (Form 1)

1. What is the capital of West Virginia?
    A. Hartford
    B. Santa Fe
    C. Harrisburg
    D. Charleston

2. What is the capital of Colorado?
    A. Raleigh
    B. Harrisburg
    C. Denver
    D. Lincoln
--snip--
```

The corresponding capitals-quiz-ans-1.txt text file will look like this:
```

1. D
2. C
3. A
4. C
--snip--
```