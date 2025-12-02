fileInput = open('day2.txt', 'r')
rangesList = fileInput.read().split(',')

sum = 0

for range in rangesList:
    start, end = range.split('-')
    while int(start) <= int(end):
        start = str(start)
        repetitions = 2
        while repetitions <= len(start):
            sequence = start[:int(len(start) / repetitions)]
            if sequence * repetitions == start:
                sum += int(start)
                break
            repetitions += 1
        start = int(start) + 1
    

print(sum)





