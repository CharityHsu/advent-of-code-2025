fileInput = open('day4.txt', 'r')
lineList = fileInput.read().split('\n')

for i, line in enumerate(lineList):
    lineList[i] = list(line)


totalRemoved = 0
while True:
    removed = 0
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
                    lineList[i][j] = '.'
                    removed += 1
    totalRemoved += removed
    if removed == 0:
        break

print(totalRemoved)



