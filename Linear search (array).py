My_Array = [99,2,17,11,19,22,50,18]
target = 11

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