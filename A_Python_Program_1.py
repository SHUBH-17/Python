arr = ["Daisy","Rose","Hyacinth","Poppy"]
myarr=[]
maxLength = len(max(arr, key=len))

for str in arr:
    if len(str) < maxLength:
        count = len(str)
        while count < maxLength:
            str += '*'
            count+=1
        myarr.append(str)
    else:
        myarr.append(str)
#print(myarr)


charBuffer = []
def processWords(input):
    s = input.split(" ")
    for i in range(0,4):
        for values in s:
            if values[i] == '0':
                continue
            else:
                charBuffer.append(values[i])
    return charBuffer

input = " ".join(map(str,myarr))
result = processWords(input)
print(*result, sep = "")
