import random

class Question:
    def __init__(self, question, option):
        self.question = question
        self.answer = option

class Quiz:
    questions = []
    def __init__(self):
        self.create_question()


    # this method creates 10 random questions and stored in questions class attribute
    def create_question(self):
        q = Question('A bird can fly', True)
        self.__class__.questions.append(q)
        q1 = Question('A dog can fly', False)
        self.__class__.questions.append(q1)
        q2 = Question('A cow can fly', False)
        self.__class__.questions.append(q2)
        q3 = Question('A bee can fly', True)
        self.__class__.questions.append(q3)
        q4 = Question('A fish can swim', True)
        self.__class__.questions.append(q4)

quiz = Quiz()
score = 0

for i in range(3):
    num = random.randint(0,5)
    q = Quiz.questions[num]
    answer = input(q.question + '(Y or N): ')
    if answer.upper() == 'Y' and q.answer :
        score += 1
        print('Yes, you got it right, your score is', score)
    else:
        print('Sorry, you got it wrong, your score is', score)

