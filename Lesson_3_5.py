arr = [2,5,6,7,8,3,2,4,5,6,1,2,3,4,9,8,7,6,5]
result = []
for i in arr:
    if i%2!=0:
        result.append (arr.index(i)+1)
print (result)