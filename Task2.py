
str = "9.8"

list_version = []


for i in range(0, len(str)):
    if(str[i] != '.'):
        list_version.append(int(str[i]))

print(list_version)

if (len(list_version) == 1):
        list_version[0] += 1
else:
       for i in range(len(list_version)-1 , -1, -1):
           if (list_version[i] + 1 != 10) and (i !=0):
               list_version[i] += 1
               break    
           else:
               list_version[i] = 0
               list_version[i-1] += 1
               break


print(list_version)
#list_version = '.'.join(str(list_version))
#print('.'.join(map(str, list_version)))