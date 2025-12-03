fileInput = open('day3.txt', 'r')
bankList = fileInput.read().split('\n')

res = 0
for bank in bankList:
    b = ['0'] * 12
    appendIndex = 0
    for i in range(len(bank)):
        if appendIndex < 12:
            b[appendIndex] = (bank[i])
            appendIndex += 1
        for index in range(appendIndex - 1, -1, -1):
            value = b[index]
            if (i - index + 12) <= len(bank) and int(bank[i]) > int(value):
                b[index] = bank[i]
                appendIndex = index + 1
    b = "".join(b)
    res += int(b)

print(res)



