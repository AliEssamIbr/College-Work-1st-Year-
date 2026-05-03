class User:

    def __init__(self, id_, username, password):

        self.__id = id_

        self.__username = username

        self.__password = password

        self.roles = []

    def __str__(self):

        return str(self.__id) + ":" + str(self.__username)

    def setPassword(self, password):

        self.password = password

    def setUsername(self, username):

        self.username = username

    def getId(self, id):

        return self.__id

    def getUsername(self, username):

        return self.__username

    def getPassword(self, password):

        return self.__password

class Admin(User):
    def __init__(self,id_,username,password):
        self.Aid = id_
        self.Ausername = username
        s = self.setPassword(password)
        if s == True:
            super().__init__(id_,username,password)
            self.roles.append("ADMIN")
            self.dept = []
            print("\nAdmin Account created succussfully!\n")
        elif s==False:
            print("\ncouldn,t create account, please try again\n")

    def setPassword(self, password):
        if len(password)<10:
            print("\npassword has to be longer than 10 characters!\n")
            return False
        else:
            self.password = password
            return True
    def __str__(self):
        temp_id = self.getId(self.Aid)
        temp_name = self.getUsername(self.Ausername)
        return f"admin "+str(temp_id) + ": " + str(temp_name)
    def addDept(self,dept):
        self.dept.append(dept)
    def removeDept(self,dept):
        self.dept.remove(dept)
    def printDeptList(self):
        print("\n\n     Departments List\n","="*30,sep="")
        c = 1
        for i in self.dept:
            print(str(c)+"- "+str(i))
            c+=1
        print("\n\n")
ali = Admin(1,"Ali","1234567890")
print(ali)
ali.addDept("BIG DATA")
ali.addDept("ENGINEERING APPLICATIONS")
ali.printDeptList()
ali.removeDept("ENGINEERING APPLICATIONS")
ali.printDeptList()










