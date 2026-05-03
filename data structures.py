My_Array = [99,2,17,11,19,22,50,18]
target = 18

def func(array,target):
    s = len(My_Array)
    for i in range(s):
        if My_Array[i] == target:
            return i
    return -1


result = func(My_Array,target)
if result != -1:
    print("\ntarget value found at index : ",result,sep="")
else:
    print("\ntarget value not found!")


s = len(My_Array)
for i in range (s - 1):
    for j in range (s - i - 1):
        if My_Array[j] > My_Array [j+1]:
            My_Array[j],My_Array[j+1] = My_Array[j+1],My_Array[j]



resultt = func(My_Array,target)
if resultt != -1:
    print("\ntarget value found at index : ",resultt,sep="")
else:
    print("\ntarget value not found!")
