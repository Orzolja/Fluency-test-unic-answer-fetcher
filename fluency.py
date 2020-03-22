Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f = open('data.txt')
TotalList = []
for word in f.read().split():
    TotalList.append(word)

print(TotalList)

unicList = ['']

for i in range(len(TotalList)):
    isItUnic = 1
    k = 0
    while k < len(unicList) and isItUnic == 1:
        if TotalList[i] == unicList[k]:
            isItUnic = 0
        k += 1
    if isItUnic == 1:
        unicList.append(TotalList[i])  

f=open('unicAnswers.txt','w')
for ele in unicList:
    f.write(ele+'\n')

f.close()
