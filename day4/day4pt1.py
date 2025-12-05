fileInput = open('day4.txt', 'r')
lineList = fileInput.read().split('\n')

result = 0

for i in range(len(lineList)):
    line = lineList[i]
    for j in range(len(line)):
        if line[j] == '@':
            numAdjacentRolls = 0
            # count number of adjacent rolls
            if i > 0:
                if j > 0:
                    if lineList[i-1][j-1] == '@':
                        numAdjacentRolls += 1
                if lineList[i-1][j] == '@':
                    numAdjacentRolls += 1
                if j < len(line) - 1:
                    if lineList[i-1][j+1] == '@':
                        numAdjacentRolls += 1
            if j > 0:
                if lineList[i][j-1] == '@':
                    numAdjacentRolls += 1
            if j < len(line) - 1:
                if lineList[i][j+1] == '@':
                    numAdjacentRolls += 1
            if i < len(lineList) - 1:
                if j > 0:
                    if lineList[i+1][j-1] == '@':
                        numAdjacentRolls += 1
                if lineList[i+1][j] == '@':
                    numAdjacentRolls += 1
                if j < len(line) - 1:
                    if lineList[i+1][j+1] == '@':
                        numAdjacentRolls += 1
            if numAdjacentRolls < 4:
                result += 1

print(result)




