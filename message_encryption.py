while True:
    check = input("Enter the Shift number : ")
    try:
        Val = int(check)
        break
    except ValueError:
        print("Invalid, eneter a number")

B = input("Enter the Test Text : ")
def Encrypt(A):
    global Val
    result = ""
    for i in A:
        if i.isupper():
            result += chr((ord(i)+Val- 65)% 26 + 65)
        elif i.islower():
            result += chr((ord(i)+Val- 97)% 26 + 97)
        else:
            result += i
    return result
def Decrypt(A):
    global Val
    Val_ = -Val
    result = ""
    for i in A:
        if i.isupper():
            result += chr((ord(i)+Val_- 65)% 26 + 65)
        elif i.islower():
            result += chr((ord(i)+Val_- 97)% 26 + 97)
        else:
            result += i
    return result
s = Encrypt(B)
print(s)
s = Decrypt(s)
print(s)
