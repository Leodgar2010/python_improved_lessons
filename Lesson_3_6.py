text = "мой дядя самых честных правил когда не в шутку занемог"
arr = text.split(" ")
arr.sort()
for k,i in enumerate(arr):
    print (k+1,i)