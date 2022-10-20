def findIndentLevel(strInput):
    spaceCount = 0
    checkIndex = 0
    if strInput != "":
        while strInput[checkIndex] == " ":
            spaceCount += 1
            checkIndex += 1
    indentLevel = int(spaceCount / 4)
    return indentLevel

def removeIndent(strInput):
    indentLevel = findIndentLevel(strInput)
    if indentLevel != 0:
        strOutput = strInput[indentLevel*5-1:]
    else:
        strOutput = strInput
    return strOutput

def findFunction(fileArrayInput, indexInput):
    arrayOutput = []
    cursorIndex = indexInput + 1
    functionIndentLevel = findIndentLevel(fileArrayInput[indexInput])
    while findIndentLevel(fileArrayInput[cursorIndex]) > functionIndentLevel:
        arrayOutput.append(fileArrayInput[cursorIndex])
        cursorIndex += 1
    return arrayOutput
    
    
    
    


inFileName = input("Input input file path... ")
outFileName = input("Input output file path... ")

inFile = open(inFileName, "r")
outFile = open(outFileName, "w")

inFileArray = inFile.readlines()

print(findFunction(inFileArray, 0))






inFile.close()
outFile.close()