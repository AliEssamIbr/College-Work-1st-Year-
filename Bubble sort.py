My_Array = [99,2,17,11,19,22,50,18]

s = len(My_Array)
for i in range (s - 1):
    for j in range (s - i - 1):
        if My_Array[j] > My_Array [j+1]:
            My_Array[j],My_Array[j+1] = My_Array[j+1],My_Array[j]
print("\nSorted array : ",My_Array,sep="")


