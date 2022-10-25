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

def findFunctionDefLines(fileArrayInput):
    arrayOutput = []
    findingFunction = False
    indentLevel = 0
    count = 0
    for line in fileArrayInput:
        if findingFunction == True and indentLevel < findIndentLevel(line):
            arrayOutput.append(count)
        else:
            indentLevel = False
        if removeSpaces(line[0:3]) == "def":
            indentLevel = findIndentLevel(line)
            findingFunction = True
            arrayOutput.append(count)
        count += 1
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

def findFunctionVarsActual(strInput):
    strOp = removeSpaces(strInput)
    arrayOutput = []
    bracketIndex = strOp.index("(")
    strOp = strOp[bracketIndex+1:-1]
    commaIndices = findCommaIndices(strOp)
    commaIndices.insert(0, -1)
    commaIndices.append(len(strOp))
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
    strOp = strInput
    count = 0
    for value in varValuesInput:
        cursorIndex = 0
        strLength = len(strOp)
        varName = varNamesInput[count]
        varNameLength = len(varName)
        while cursorIndex < strLength - varNameLength:
            testStr = strOp[cursorIndex:cursorIndex + varNameLength]
            if testStr == varName and checkVar(cursorIndex, varName, strOp):
                strOp = replaceByIndex(value, varName, strOp, cursorIndex)
            cursorIndex += 1
            strLength = len(strOp)
        count += 1
    return strOp

def findFunctionInLine(functionInput, strInput):
    arrayOutput = []
    functionLength = len(functionInput)
    cursorIndex = 0
    while cursorIndex < len(strInput) - functionLength:
        if strInput[cursorIndex : cursorIndex + functionLength] == functionInput:
            arrayOutput.append(cursorIndex)
        cursorIndex += 1
    return arrayOutput

def findFunctionActual(strInput, indexInput):
    cursorIndex = indexInput
    bracketsCount = 0
    while strInput[cursorIndex] != "(":
        cursorIndex += 1
    cursorIndex += 1
    bracketsCount += 1
    while bracketsCount > 0:
        if strInput[cursorIndex] == "(":
            bracketsCount += 1
        elif strInput[cursorIndex] == ")":
            bracketsCount -= 1
        cursorIndex += 1
    return cursorIndex
    

inFileName = input("Input input file path... ")
outFileName = input("Input output file path... ")

inFile = open(inFileName, "r")
outFile = open(outFileName, "w")

inFileArray = inFile.readlines()
inFileArray.append("#END OF FILE")

inFileArray = removeNextLine(inFileArray)

functionIndices = findFunctionIndices(inFileArray)
functionDefIndices = findFunctionDefLines(inFileArray)

varNameCount = 0
varNameCountArray = []

for index in functionIndices:
    functionName = findFunctionName(removeIndent(inFileArray[index]))
    functionVars = findFunctionVars(removeIndent(inFileArray[index]))
    functionLinesIndents = removeIndent(findFunctionLines(inFileArray, index))
    functionLines = []
    for line in functionLinesIndents:
        functionLines.append(removeIndent(line))

    arrayLength = len(inFileArray)
    mainStartIndex = 0
    count = 0
    while count < arrayLength:
        
        if not(count in functionDefIndices):
            mainStartIndex = count
            line2 = inFileArray[count]
            functionIndicesInLine = findFunctionInLine(functionName, line2)
            for index2 in functionIndicesInLine:
 
                startIndex = index2
                endIndex = findFunctionActual(line2, index2)
                arrayFunctionValues = findFunctionVarsActual(line2[startIndex:endIndex]) 
                arrayReplace = []
                for count2 in range(len(functionLinesIndents)):
                    functionLine = functionLinesIndents[count2]
                    arrayReplace.append(replaceVars(functionVars, arrayFunctionValues, functionLine))
                
                for count3 in range(len(arrayReplace)):
                    varName = "var" + str(varNameCount)
                    varNameCountArray.append(varName)
                    arrayReplace[count3] = removeIndent(arrayReplace[count3])
                    if arrayReplace[count3][0:6] == "return":
                        arrayReplace[count3] = arrayReplace[count3][6:]
                        arrayReplace[count3] = varName + " = " + arrayReplace[count3]
                        varNameCount += 1
                
                #TODO: replace functions with var names
                
                count4 = 0
                for count3 in range(len(arrayReplace)):
                    inFileArray.insert(mainStartIndex, arrayReplace[count3])
                    mainStartIndex += 1
                    count4 += 1
                count += count4
        arrayLength = len(inFileArray)
        count += 1
        
        
        
for line in inFileArray:
    print(line)
            
    #TODO: find function name, find spot before var definitions, put function stuffs outputting into variable
    #replace said variable into function usage in found function
    #CONTINUE HERE
    
    
    
    





inFile.close()
outFile.close()