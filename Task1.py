import copy

str = "[['XXX', 1], ['XXXXXX', 6], ['X', 2], ['XXXXXX', 8], ['X', 3], ['XXX', 1]], 4"


listFreeChairs = []
countChairs = int(str[len(str)-1])
countFreeChairs = 0
listChairs = []

startIndex = 0

while str.find('[', startIndex) != -1:

    tempStr = str[str.find('[', startIndex): str.find(']', startIndex) + 1]

    if (int(tempStr[len(tempStr)-2]) - tempStr.count('X')) >= 0:

        listFreeChairs.append(int(tempStr[len(tempStr)-2]) - tempStr.count('X'))
    else:
        listFreeChairs.append(0)


    startIndex = (str.find(']', startIndex)) + 1
    #print(tempStr)



for i in listFreeChairs:  
  
   countFreeChairs += i

print(listFreeChairs)
print("Количество свободных - ", countFreeChairs)
print("количество нужных - ", countChairs)

if (countFreeChairs - countChairs) >= 0:
    if (countFreeChairs == countChairs):
        print("Необходимо взять все ", listFreeChairs)
    else:
        i=0

        while countChairs != 0:
            if (countChairs - listFreeChairs[i]) >= 0:
                countChairs -= listFreeChairs[i]
                listChairs.append(listFreeChairs[i])
                i += 1
            else:
                listChairs.append(countChairs)
                countChairs = 0

        print("Необходимо взять ", listChairs)

    
    
elif countChairs == 0:
    print("Стулья не нужны")
else:
    print("Недостаточно!")
