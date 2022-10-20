class userDefinedFunction:
    def __init__(self, functionName, functionVars, functionLines):
            self.name = functionName
            self.vars = functionVars
            self.lines = functionLines


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

def removeNextLine(arrayInput):
    arrayOperation = arrayInput
    for number in range(len(arrayOperation)-2):
        item = arrayOperation[number]
        arrayOperation[number] = item[0:-1]
    return arrayOperation

def findFunctionLines(fileArrayInput, indexInput):
    arrayOutput = []
    cursorIndex = indexInput + 1
    functionIndentLevel = findIndentLevel(fileArrayInput[indexInput])
    while findIndentLevel(fileArrayInput[cursorIndex]) > functionIndentLevel:
        arrayOutput.append(fileArrayInput[cursorIndex])
        cursorIndex += 1
    return arrayOutput
    
def findFunctionIndices(fileArrayInput):
    cursorIndex = 0
    arrayOutput = []
    for line in fileArrayInput:
        rawLine = removeIndent(line)
        if rawLine [0:3] == "def":
            arrayOutput.append(cursorIndex)
        cursorIndex += 1
    return arrayOutput

def removeSpaces(strInput):
    strOp = strInput.replace(" ","")
    return strOp
    
def findFunctionName(strInput):
    strOp = removeSpaces(strInput)
    bracketIndex = strOp.index("(")
    functionName = strOp[3:bracketIndex]
    return functionName
    
    


inFileName = input("Input input file path... ")
outFileName = input("Input output file path... ")

inFile = open(inFileName, "r")
outFile = open(outFileName, "w")

inFileArray = inFile.readlines()
inFileArray.append("#END OF FILE")

inFileArray = removeNextLine(inFileArray)

functionIndices = findFunctionIndices(inFileArray)

for index in functionIndices:
    functionName = findFunctionName(inFileArray[index])
    functionLines = findFunctionLines(inFileArray, index)






inFile.close()
outFile.close()