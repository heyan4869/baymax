__author__ = 'Yan'

from scanner import *
from math import *
import parser

def testGrader():
    ## answer should be extracted from the student's homework
    ## and return as a string
    # str = imageReader()

    ## currently we use a presigned string for testing the function
    ocrresult = "12 + 5 - 2 * ( 7 - 1 ) = 5"

    ## split the answer and get the formula as well as the answer
    # use partition instead of split on the string
    diffpart = ocrresult.partition("=")

    ## get the question and answer part
    questionpart = diffpart[0]
    question = parser.expr(questionpart).compile()
    correctresult = eval(question)

    answerpart = diffpart[2]
    # answer = parser.expr(answerpart).compile()
    studentresult = eval(answerpart)

    if correctresult == studentresult:
        return True
    else:
        return False

checkresult = testGrader()
print checkresult