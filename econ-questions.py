#!/usr/bin/python
import random
class Question(object):

  def __init__(self, number, question, choices):
    self.number = number
    self.question = question
    self.A = choices[0]
    self.B = choices[1]
    self.C = choices[2]
    self.D = choices[3]

  def setAnswer(self, answer):
    self.answer = answer

  def printQuestion(self):
    numStr = self.number
    if (int(self.number) < 100): numStr = numStr[1:]
    if (int(self.number) < 10): numStr = numStr[1:]
    print "-------------------"
    print numStr + ": " + self.question
    print "A) " + self.A
    print "B) " + self.B
    print "C) " + self.C
    print "D) " + self.D
    print "-------------------"
  
  def promptAnswer(self, count):
    choice = raw_input("Your answer: ")
    choice = choice.strip()
    answer = self.answer
    answer = answer.strip()
    congrats = ["You got it!","Good job!",
                "You are gonna ace this test!",
                "That's right!","Correct!",
                "So smart!"]
    woops = ["ehh, guess again.",
             "Sorry thats not it.",
             "Nope...","Not Quite"]
    self.score = 20-((count)*5)
    if choice == answer or choice.upper() == answer:
      print congrats[random.randint(0,len(congrats)-1)]
      return self.score
    else:
      print woops[random.randint(0,len(woops)-1)]
      if count == 2:
        print "The answer was: " + answer
        return self.score
      return self.promptAnswer(count+1)

class Quizzer(object):

  def __init__(self, filename):
    self.readQuestionFile(filename)

  def readQuestionFile(self, filename):
    fd = open(filename, "r")
    self.questions = []
    self.answers = []
    line = fd.readline()
    while (line):
      if (line.strip() == "!!ANSWERS!!"):
        line = fd.readline()
        while (line):
          self.parseAnswers(line)
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
          self.questions.append(q)
        line = fd.readline()
    fd.close()

  def parseAnswers(self, line):
    answerNumber = line[0:2]
    answerChar = line[5:]
    answer = [answerNumber, answerChar]
    self.answers.append(answer)

  def setAnswers(self):
    for i in range(len(self.questions)):
      question = self.questions[i]
      numStr = question.number
      if int(numStr) < 100: numStr = numStr[1:]
      if int(numStr) < 10: numStr = numStr[1:]
      answer = self.answers[int(numStr)-1]
      question.setAnswer(answer[1])

  def getRandomQuestions(self, number):
    randomQuestions = []
    for i in range(int(number)):
      randomQuestion = self.questions[random.randint(0, len(self.questions)-1)]
      randomQuestions.append(randomQuestion)
    return randomQuestions

  def runMenu(self):
    print("Please select a game mode: ")
    print("1. Normal Mode")
    print("2. Random Mode")
    print("\"exit\" to exit")
    mode = raw_input("> ")
    mode = mode.strip()
    if mode == "exit": return None
    number = raw_input("How many questions would you like? 1-256> ").strip()
    while not number.isdigit():
      number = raw_input("How many questions would you like? 1-256> ").strip()
    if number == "0":
      self.runMenu()
    elif int(number) > 256:
      print "We don't have %s questions, but here's 256." % number
      number = "256"
    if mode == "1":
      #Normal mode
      return self.questions[0:int(number)]
    elif mode == "2":
      #Random mode
      rand = self.getRandomQuestions(number)
      return rand
    else:
      print "Not a valid choice option."
      self.runMenu()

def main():
  quizzer = Quizzer("econ-questions.txt")
  quizzer.setAnswers()
  print("Hello, welcome to Econ2 Multiple Choice Quiz Game")
  while 1:
    gameQuestions = quizzer.runMenu()
    score = 0
    total = 0
    if (gameQuestions):
      for q in gameQuestions:
        q.printQuestion()
        score = q.promptAnswer(0)
        total = total + score
      maxScore = len(gameQuestions)*20
      percent = float(total*100)/float(maxScore)
      print "Score: " + str(percent) + "%"
    else: return 0

if __name__ == "__main__":
  main()
