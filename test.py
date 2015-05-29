__author__ = 'Yan'

ocrresult = "12 + 5 - 2 * ( 7 - 1 ) = 5 \n 3 * 2 - 4 = 2"
diffline = ocrresult.split("\n")
for i in diffline:
    print(i)
