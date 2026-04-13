
class variables:
    def __init__(self,variable):
        self.variable = variable
        if type(variable) == list:
            self.ismatrix = True
        else:
            self.ismatrix = False
    def __str__(self):
        if self.ismatrix == True:
            return f"the variable's values are {self.variable} and it is a Matrix/List"
        else:
            return f"the variable's value is {self.variable} and it is an integer"
    def __mul__(self,other_variable):
        if self.ismatrix == True and other_variable.ismatrix == True:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] * other_variable.variable[i][j]
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == True and other_variable.ismatrix == False:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] * other_variable.variable 
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == True:
            result = []
            for i in range(len(other_variable.variable)):
                sub_result = []
                for j in range(len(other_variable.variable[i])):
                    multiply = other_variable.variable[i][j] * self.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == False:
            return self.variable * other_variable.variable
        else:
            return "error, invalid variables"
    def __add__(self,other_variable):
        if self.ismatrix == True and other_variable.ismatrix == True:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] + other_variable.variable[i][j]
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == True and other_variable.ismatrix == False:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] + other_variable.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == True:
            result = []
            for i in range(len(other_variable.variable)):
                sub_result = []
                for j in range(len(other_variable.variable[i])):
                    multiply = other_variable.variable[i][j] + self.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == False:
            return self.variable + other_variable.variable
        else:
            return "error, invalid variables"
    def __sub__(self,other_variable):
        if self.ismatrix == True and other_variable.ismatrix == True:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] - other_variable.variable[i][j]
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == True and other_variable.ismatrix == False:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] - other_variable.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == True:
            result = []
            for i in range(len(other_variable.variable)):
                sub_result = []
                for j in range(len(other_variable.variable[i])):
                    multiply = other_variable.variable[i][j] - self.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == False:
            return self.variable - other_variable.variable
        else:
            return "error, invalid variables"
    def __truediv__(self,other_variable):
        if self.ismatrix == True and other_variable.ismatrix == True:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] / other_variable.variable[i][j]
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == True and other_variable.ismatrix == False:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] / other_variable.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == True:
            result = []
            for i in range(len(other_variable.variable)):
                sub_result = []
                for j in range(len(other_variable.variable[i])):
                    multiply = other_variable.variable[i][j] / self.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == False:
            return self.variable / other_variable.variable
        else:
            return "error, invalid variables"
    def __floordiv__(self,other_variable):
        if self.ismatrix == True and other_variable.ismatrix == True:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] // other_variable.variable[i][j]
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == True and other_variable.ismatrix == False:
            result = []
            for i in range(len(self.variable)):
                sub_result = []
                for j in range(len(self.variable[i])):
                    multiply = self.variable[i][j] // other_variable.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == True:
            result = []
            for i in range(len(other_variable.variable)):
                sub_result = []
                for j in range(len(other_variable.variable[i])):
                    multiply = other_variable.variable[i][j] // self.variable
                    sub_result.append(multiply)
                result.append(sub_result)
            return result
        if self.ismatrix == False and other_variable.ismatrix == False:
            return self.variable // other_variable.variable
        else:
            return "error, invalid variables"
    
a = variables([[1,2,3],[4,5,6]])
b = variables([[7,8,9],[1,2,3]])
c = variables([[1,2,3],[7,8,9]])
d = variables(5)
e = variables(10)
print(a*b)
print(a*c)
print(b*c)

print(a)
print(b)
print(c)
print(d)

print(a*d)
print(d*b)
print(d*e)
print(e*d)

print(a+b)
print(b+a)
print(a+d)
print(d+a)
print(d+e)

print(a-b)
print(b-a)
print(a-d)
print(d-a)
print(d-e)
print(e-d)

print(a/b)
print(b/a)
print(a/d)
print(d/a)
print(d/e)
print(e/d)

print(a//b)
print(b//a)
print(a//d)
print(d//a)
print(d//e)
print(e//d)