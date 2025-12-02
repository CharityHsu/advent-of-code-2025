fileInput = open('day1.txt', 'r')
rotationList = fileInput.read().split('\n')

current = 50
result = 0

for r in rotationList:
    direction = r[0]
    amount = int(r[1:])
    if direction == 'R':
        current += amount
        while current > 99:
            current -= 100
            result += 1
    else: # left
        if current == 0: 
            result -= 1
        current -= amount
        while current < 0:
            current += 100
            result += 1
        if current == 0:
            result += 1
    
    

print(result)




