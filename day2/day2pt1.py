fileInput = open('day2.txt', 'r')
rangesList = fileInput.read().split(',')

sum = 0

for range in rangesList:
    start, end = range.split('-')
    while int(start) <= int(end):
        start = str(start)
        if len(start) % 2 == 0: 
            halfway = int(len(start)/2)
            sub1 = start[:halfway]
            sub2 = start[halfway:]
            if sub1 == sub2:
                sum += int(start)
        start = int(start) + 1
    

print(sum)





