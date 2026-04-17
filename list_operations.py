import random as rd
original_array = []
for _ in range(100):
    original_array.append(rd.randint(0,1000))
def threshold_search(array):
    while True:
        threshold_input = input("\nenter the threshold : ")
        try:
            threshold_input1 = int(threshold_input)
            break
        except ValueError:
            print("INVALID, ENTER AN INTEGER\n")
    threshold_array = []
    for i in array:
        if i >=threshold_input1:
            threshold_array.append(i)
    if threshold_array==[]:
        return f"Threshold value exceeds all values in array!"
    return threshold_array
def ordered(array):
    for s in range(len(array)):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1]=array[i+1],array[i]
    return array
def duplicate_remove(array):
    for s in range(len(array)):
        for i in range(len(array)-1):
            if array[i] == array[i+1]:
                array.pop(i+1)
                break
    return array
def data_normalization(array):
    temp = int
    normalized = []
    if len(array) > 1:
        for i in range(len(array)-1):
            if array[i] <= array[i+1]:
                temp = array[i+1]
    else:
        temp = array[0]
    for i in array:
        normal = i/temp
        normalized.append(round(normal,4))
    return normalized
z = threshold_search(original_array)
print("\nthreshold result : \n",z)
if z == "Threshold value exceeds all values in array!":
    pass
else:
    print("\nordered list : \n",ordered(z))
    print("\nduplicate removal : \n",duplicate_remove(z))
    print("\nnormalized data : \n",data_normalization(z))
print("\n\n-----------------------------------\n        original list\n")
print(original_array)
print("\nordered list : \n",ordered(original_array))
print("\nduplicate removal : \n",duplicate_remove(original_array))
print("\nnormalized data : \n",data_normalization(original_array))