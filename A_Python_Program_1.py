arr = ["Daisy","Rose","Hyacinth","Poppy"]
myarr=[]
maxLength = len(max(arr, key=len))

for str1 in arr:
    if len(str1) < maxLength:
        count = len(str1)
        while count < maxLength:
            str1 += '*'
            count+=1
        myarr.append(str1)
    else:
        myarr.append(str1)
print(myarr)
input = " ".join(map(str,myarr))
print(input)

charBuffer = []
def processWords(input,maxlen):
    s = input.split(" ")
    for i in range(0,maxlen):
        for values in s:
            if values[i] == '0':
                continue
            else:
                charBuffer.append(values[i])
    return charBuffer

#input = " ".join(map(str,arr))
result = processWords(input,maxLength)
print(*result, sep = "")
