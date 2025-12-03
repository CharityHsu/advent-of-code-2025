fileInput = open('day3.txt', 'r')
bankList = fileInput.read().split('\n')


res = 0

for bank in bankList:
    b1, b2 = int(bank[0]), int(bank[1])
    for i in range(1, len(bank)):
        if int(bank[i]) > b2:
            b2 = int(bank[i])
        if i < len(bank) - 1 and int(bank[i]) > b1:
            b1 = int(bank[i])
            b2 = int(bank[i + 1])
    print(b1 * 10 + b2)
    res += (b1 * 10 + b2)



print(res)




