#!/usr/bin/python
import random
class Question(object):
  def __init__(self, number, question, answers):
    self.number = number
    self.question = question
    self.answerA = answers[0]
    self.answerB = answers[1]
    self.answerC = answers[2]
    self.answerD = answers[3]

  def setCorrectAnswer(self, correctAnswer):
    self.correctAnswer = correctAnswer

  def printQuestion(self):
    print "------------------------------------------"
    print self.number + ": " + self.question
    self.printChoices()

  def printChoices(self):
    print "A) " + self.answerA
    print "B) " + self.answerB
    print "C) " + self.answerC
    print "D) " + self.answerD
    print "------------------------------------------"

def readQuestionFile(filename):
  fd = open(filename, "r")
  print "Name of file: ", fd.name
  questions = []
  answers = []
  line = fd.readline()
  while (line):
    if (line.strip() == "!!ANSWERS!!"):
      line = fd.readline()
      while (line):
        answerNumber = line[0] + line[1] + line[2]
        correctAnswer = line[5:]
        correct = [answerNumber, correctAnswer]
        answers.append(correct)
        line = fd.readline()
      line = None
    else:
      firstDesc = line.split()[0]
      firstDesc = firstDesc[0:-1]
      if (firstDesc.isdigit()):
        number = firstDesc
        quest = line
        quest = quest[5:]
        A = fd.readline()
        B = fd.readline()
        C = fd.readline()
        D = fd.readline()
        choices = [A[3:], B[3:], C[3:], D[3:]]
        q = Question(number, quest, choices)
        questions.append(q)

      line = fd.readline()

  fd.close()
  return questions, answers

def promptQuestion(question):
  question.printQuestion()
  choice = raw_input("Your answer: ")
  choice = choice.strip()
  answer = question.correctAnswer
  answer = answer.strip()
  congrats = ["You got it!", "Good job!", "You are gonna ace this test!", "That's right!"
      , "Correct!", "So smart!"]
  woops = ["ehh, guess again.", "Sorry thats not it.", "Nope...", "Not Quite"]
  if choice == answer or choice.upper() == answer:
    print congrats[random.randint(0,len(congrats)-1)]
  else:
    print woops[random.randint(0,len(woops)-1)]

def setAnswers(questions, answers):
  for i in range(len(questions)):
    question = questions[i]
    numStr = question.number
    if int(numStr) < 100: numStr = numStr[1:]
    if int(numStr) < 10: numStr = numStr[1:]
    answer = answers[int(numStr)-1]
    question.setCorrectAnswer(answer[1])

def main():
  questions, answers = readQuestionFile("econ-questions.txt")
  setAnswers(questions, answers)
  for q in questions:
    promptQuestion(q);

if __name__ == "__main__":
  main()
