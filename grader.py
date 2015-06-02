__author__ = 'Yan'

from ImageScan import *
from math import *
import parser

# if the ocr api could use a new line symbol \n to seperate different lines
def testgradernewline():
    # answer should be extracted from the student's homework
    # and return as a string
    # str = imagereader()

    # currently use a presigned string for testing the function
    ocrresult = "12 + 5 - 2 * ( 7 - 1 ) = 5 \n 5 * 2 - 4 = 6 \n 5 - 4 / 2 = 1"

    # when dealing with multiple questions and answers
    # split the string with \n first
    diffline = ocrresult.split(" \n ")
    numofline = len(diffline)
    # save all the check result in a list
    checkresult = []

    # process each line as individual questions
    # the head of each line must not be blankspace
    for eachline in diffline:
        # split the answer and get the formula as well as the answer
        # use partition instead of split on the string
        diffpart = eachline.partition("=")

        # get the question and answer part
        questionpart = diffpart[0]
        question = parser.expr(questionpart).compile()
        correctresult = eval(question)

        answerpart = diffpart[2]
        # answer = parser.expr(answerpart).compile()
        studentresult = eval(answerpart)

        if correctresult == studentresult:
            checkresult.append(True)
        else:
            checkresult.append(False)

    # return the result of grade in the format of a list
    return checkresult


# in case the new line symbol \n is not available in the ocr api
# but just use a black to seperate different lines
def testgraderspace():
    # answer should be extracted from the student's homework
    # and return as a string
    # str = imagereader()

    # currently use a presigned string for testing the function
    ocrresult = "12 + 5 - 2 * ( 7 - 1 ) = 5 5 * 2 - 4 = 6 5 - 4 / 2 = 1"

    # when dealing with multiple questions and answers
    # split the question and answer pair with space first
    diffline = ocrresult.split(" = ")
    num = len(diffline)
    # print len(diffline)

    for i in range(1, num - 1):
        currline = diffline[i]
        diffpart = currline.split(" ", 1)
        diffline[i - 1] = diffline[i - 1] + " = " + diffpart[0]
        diffline[i] = diffpart[1]

    diffline[num - 2] = diffline[num - 2] + " = " + diffline[num - 1]

    # save all the check result in a list
    checkresult = []

    # with the appropriate question answer pair, check if the answer is right
    for temp in range(0, num - 1):
        eachline = diffline[temp]
        # split the answer and get the formula as well as the answer
        # use partition instead of split on the string
        diffpart = eachline.partition("=")

        # get the question and answer part
        questionpart = diffpart[0]
        question = parser.expr(questionpart).compile()
        correctresult = eval(question)

        answerpart = diffpart[2]
        # answer = parser.expr(answerpart).compile()
        studentresult = eval(answerpart)

        if correctresult == studentresult:
            checkresult.append(True)
        else:
            checkresult.append(False)

    # return the result of grade in the format of a list
    return checkresult



result = testgraderspace()
print "The number of question is: "
print len(result)
print "The result of each answer is: "
for i in result:
    print i


