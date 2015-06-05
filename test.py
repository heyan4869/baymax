import parser

ocrresult = "12 + 5 - 2 * ( 7 - 1 ) = 5 5 * 2] - 4 = 6 5 - 4 / 2 = 1"
diffline = ocrresult.split(" = ")
num = len(diffline)
# print len(diffline)

for i in range(1, num - 1):
    currline = diffline[i]
    diffpart = currline.split(" ", 1)
    diffline[i - 1] = diffline[i - 1] + " = " + diffpart[0]
    diffline[i] = diffpart[1]

diffline[num - 2] = diffline[num - 2] + " = " + diffline[num - 1]

checkresult = []
for temp in range(0, num - 1):
    eachline = diffline[temp]
    print eachline
    # split the answer and get the formula as well as the answer
    # use partition instead of split on the string
    diffpart = eachline.partition("=")

    # get the question and answer part
    questionpart = diffpart[0]
    # question = parser.expr(questionpart).compile()
    try:
        correctresult = eval(questionpart)
        print correctresult
        answerpart = diffpart[2]
        # answer = parser.expr(answerpart).compile()
        studentresult = eval(answerpart)

        if correctresult == studentresult:
            checkresult.append(True)
        else:
            checkresult.append(False)
    except (SyntaxError, ValueError):
        print "OCR formula error"




