import string

def checkVar(varIndex, varName, strInput):
    varNameLength = len(varName)
    strInputProcessed = " " + strInput + " "
    strOperation = strInputProcessed[varIndex:varIndex + varNameLength + 2]
    if not(strOperation[0] in string.ascii_lowercase) and not(strOperation[-1] in string.ascii_lowercase) and strOperation[1:-1] == varName and checkQuoteCount(strInput, varIndex):
        return True
    else:
        return False

def checkQuoteCount(strInput, indexInput):
    count1 = 0
    count2 = 0
    for index in range(indexInput):
        if strInput[index] == "'":
            count1 += 1
        if strInput[index] == '"':
            count2 += 1
    if count1%2 == 0 and count2%2 == 0:
        return True
    else: 
        return False

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
    
def findCommaIndices(strInput):
    strOp = removeSpaces(strInput)
    arrayOutput = []
    cursorIndex = 0
    while cursorIndex < len(strOp):
        if strOp[cursorIndex] == ",":
            arrayOutput.append(cursorIndex)
        cursorIndex += 1
    return arrayOutput

def findFunctionVars(strInput):
    strOp = removeSpaces(strInput)
    arrayOutput = []
    bracketIndex = strOp.index("(")
    strOp = strOp[bracketIndex+1:-1]
    commaIndices = findCommaIndices(strOp)
    commaIndices.insert(0, -1)
    commaIndices.append(-1)
    cursorIndex = 1
    while cursorIndex < len(commaIndices):
        startIndex = commaIndices[cursorIndex-1]
        stopIndex = commaIndices[cursorIndex]
        varName = strOp[startIndex+1:stopIndex]
        arrayOutput.append(varName)
        cursorIndex += 1
    return arrayOutput

def replaceByIndex(replacerInput, replaceeInput, strInput, replaceeIndex):
    strOp = strInput
    strOp = strOp[:replaceeIndex] + replacerInput + strOp[replaceeIndex + len(replaceeInput):] #START HERE
    return strOp
    

def replaceVars(varNamesInput, varValuesInput, strInput):
    return

inFileName = input("Input input file path... ")
outFileName = input("Input output file path... ")

inFile = open(inFileName, "r")
outFile = open(outFileName, "w")

inFileArray = inFile.readlines()
inFileArray.append("#END OF FILE")

inFileArray = removeNextLine(inFileArray)

functionIndices = findFunctionIndices(inFileArray)

for index in functionIndices:
    functionName = findFunctionName(removeIndent(inFileArray[index]))
    functionVars = findFunctionVars(removeIndent(inFileArray[index]))
    functionLinesIndents = removeIndent(findFunctionLines(inFileArray, index))
    functionLines = []
    for line in functionLinesIndents:
        functionLines.append(removeIndent(line))
    
    print(functionName)
    print(functionVars)
    print(functionLines)
    
    





inFile.close()
outFile.close()