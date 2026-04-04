my_array = [7, 12, 9, 4, 11]
minVal = my_array[0] 
maxVal = my_array[0]
for i in my_array: 
    if i < minVal: 
        minVal = i
for i in my_array: 
    if i > maxVal: 
        maxVal = i
print("Lowest value: ",minVal,"\nHighest Value: ",maxVal,sep="")