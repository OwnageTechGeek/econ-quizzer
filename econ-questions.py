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
    numStr = self.number
    if (int(self.number) < 100): numStr = numStr[1:]
    if (int(self.number) < 10): numStr = numStr[1:]
    print "------------------------------------------"
    print numStr + ": " + self.question
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
        parseAnswers(line, answers)
        line = fd.readline()
      
      line = None
    else:
      desc = line.split()[0]
      desc = desc[0:-1]
      if (desc.isdigit()):
        quest = line[5:]
        A = fd.readline()
        B = fd.readline()
        C = fd.readline()
        D = fd.readline()
        choices = [A[3:], B[3:], C[3:], D[3:]]
        q = Question(desc, quest, choices)
        questions.append(q)
    
      line = fd.readline()
  fd.close()
  return questions, answers

def parseAnswers(line, answers):
  answerNumber = line[0:2]
  correctAnswer = line[5:]
  answer = [answerNumber, correctAnswer]
  answers.append(answer)

def setAnswers(questions, answers):
  for i in range(len(questions)):
    question = questions[i]
    numStr = question.number
    if int(numStr) < 100: numStr = numStr[1:]
    if int(numStr) < 10: numStr = numStr[1:]
    answer = answers[int(numStr)-1]
    question.setCorrectAnswer(answer[1])

def promptAnswer(question, count, scores):
  choice = raw_input("Your answer: ")
  choice = choice.strip()
  answer = question.correctAnswer
  answer = answer.strip()
  congrats = ["You got it!","Good job!","You are gonna ace this test!",
      "That's right!","Correct!","So smart!"]
  woops = ["ehh, guess again.","Sorry thats not it.","Nope...","Not Quite"]
  score = 30//(count+2)
  if choice == answer or choice.upper() == answer:
    print congrats[random.randint(0,len(congrats)-1)]
    scores.append(score)
  else:
    print woops[random.randint(0,len(woops)-1)]
    if count == 2:
      print "The answer was: " + answer
      scores.append(score)
      return
    promptAnswer(question, count+1, scores)

def getRandomQuestions(questions, number):
  randomQuestions = []
  for i in range(number):
    randomQuestion = questions[random.randint(0, len(questions)-1)]
    randomQuestions.append(randomQuestion)

  return randomQuestions

def main():
  questions, answers = readQuestionFile("econ-questions.txt")
  setAnswers(questions, answers)
  #for q in questions:
  #  promptQuestion(q)
  numQuestions = 5
  rand = getRandomQuestions(questions, numQuestions)
  score = 0
  scores = []
  for r in rand:
    r.printQuestion()
    promptAnswer(r, 0, scores)
    
  for i in range(len(scores)):
    score = score + scores[i]
  maxScore = numQuestions*15
  total = float(score*100)/float(maxScore)
  
  print "Score: " + str(total) + "%"

if __name__ == "__main__":
  main()
