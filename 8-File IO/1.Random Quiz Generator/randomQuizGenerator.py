#! python3

import random

# quiz data
# keys - states, values - capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# generate 35 quiz files
for quiz in range(35):
    # Create the quiz and answer key files
    quizFile = open('capitals-quiz-%s.txt' % (quiz + 1), 'w')
    quizAnsFile = open('capitals-quiz-ans-%s.txt' % (quiz + 1), 'w')

    # Write the header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quiz + 1))
    quizFile.write('\n\n')

    # Shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # generate the 50 questions
    for question in range(50):
        correctAnswer = capitals[states[question]]
        wrongAnswers = list(capitals.values())
        # delete the correct answer from the list of wrong ans
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        # select 3 wrong ans
        wrongAnswers = random.sample(wrongAnswers, 3)
        # add the correct ans to options
        ansOptions = wrongAnswers + [correctAnswer]
        # shuffle the options
        random.shuffle(ansOptions)

        # write the question and options to the file
        quizFile.write('%s. What is the capital of %s?\n' % (question + 1, states[question]))
        for i in range(4):
            # print option A) option1, B) option 2
            quizFile.write(' %s) %s\n' % ('ABCD'[i], ansOptions[i]))
        quizFile.write('\n')
        
        # write the answers to the answer key file
        quizAnsFile.write(' %s) %s\n' % (question+1, 'ABCD'[ansOptions.index(correctAnswer)]))

    # close the files (in outer for loop)
    quizFile.close()
    quizAnsFile.close()
