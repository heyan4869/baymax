import parser

ocrresult = "12 + 5 - 2 * ( 7 - 1 ) = 5 5 * 2 - 4 = 6 5 - 4 / 2 = 1"
diffline = ocrresult.split(" = ")
num = len(diffline)
print len(diffline)

for i in range(1, num - 1):
    currline = diffline[i]
    diffpart = currline.split(" ", 1)
    diffline[i - 1] = diffline[i - 1] + " = " + diffpart[0]
    diffline[i] = diffpart[1]

diffline[num - 2] = diffline[num - 2] + " = " + diffline[num - 1]

for temp in range(0, num - 1):
    eachline = diffline[temp]
    print eachline
