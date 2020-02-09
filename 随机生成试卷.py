# 创建35份随机的试卷
import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


# Generate 35 quiz files
for quizNum in range(35):
    # create the quiz and answer key file
    quizFile = open('C:\\Users\\97440\\Desktop\\data\\capitalsquiz%s.txt' %(quizNum + 1), 'w')
    answerKeyFile = open('C:\\Users\\97440\\Desktop\\data\\capitalsquiz_answer%s.txt' %(quizNum + 1), 'w')
    
    # Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capital Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    #shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)  
    # 创建答案选项
    for questionNum in range(50):

        # get right and worng answers
        correctAnswer = capitals[states[questionNum]]

        worngAnswers = list(capitals.values())
        del worngAnswers[worngAnswers.index(correctAnswer)]
        worngAnswers = random.sample(worngAnswers, 3)

        answerOptions  = worngAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # 写入试卷和答案
        # write the question and the answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # write the answer key to a file
        answerKeyFile.write('%s. %s\n' %(questionNum + 1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
        
