x =[]
class books:
    def __init__(self):
     self.data = {}
     self.author_data = {}
    def add_item(self,book_title, author, available):
       self.data[book_title] = {
          "info" : {
            "title" : book_title,
            "author" : author,
            "available" : available
          }

       }
    def add_title(self,author, title, available):
        checker = self.author_data.get(author)
        if not checker:
            self.author_data[author] = {
            "info" : {
                "title" : [title,],
                "available" : available
            }
            }
        else:
            self.author_data[author]["info"]["title"].append(title)
    def author_check(self, author, keys=None):
        booke = self.author_data.get(author)
        if  not booke:
            return "no"
        info = booke["info"]
        if keys:
            return {k: info[k] for k in keys if k in info}
        return info
    def check(self, book_title, keys=None):
        booke = self.data.get(book_title)
        if  not booke:
            return "no"
        info = booke["info"]
        if keys:
            return {k: info[k] for k in keys if k in info}
        return info
    def borrowing(self,book_title):
        if book_title in self.data:
            self.data[book_title]["info"]["available"] = False
    def unborrowing(self, book_title):
        if book_title in self.data:
               self.data[book_title]["info"]["available"] = True
def returning():
   z = (input("please enter the name of the book you'd like to return! \n"))
   book1.unborrowing(z)
def checking():
        x = (input("please enter the book you'd like to check for : "))
        result = book1.check(x)
        if result == "no":
            print("\n\nsorry, but we couldn't find that book!\n\n")
        else:
            title = x
            author = result["author"]
            avail = result["available"]
            if avail == True:
                avail = "available"
            elif avail == False:
                avail = "not available"
            print("\nthe book ", title, " by ", author, " is "+ avail + "!\n", sep= "'" )
def add_book():
    new_title = str(input("please enter the title of the new book you'd like to add!\n"))
    new_author = str(input("please enter the author of the new book you'd like to add!\n")) 
    book1.add_item(new_title,new_author, available=True)  
    book1.add_title(new_author,new_title, available=True)
def borrow():
    z = (input("please enter the title of the book you'd like to borrow! \n"))
    book1.borrowing(z)
def search():
    z = input("\nplease enter the name of the author you're searching about! \n")
    result = book1.author_check(z)
    if result == "no":
        print("\nsorry! we couldn't find that author!\n")
    else:
        print ("\nthe author ",z," has written the following books : ", sep="'")
        for n in result["title"]:
            print(n)
def library():
    print("\n--- Full Library Catalog ---")
    if not book1.data:
        print("The library is currently empty.")
        return

    for book_title in book1.data:
        
        result = book1.check(book_title)
        author = result["author"]
        if result["available"]:
            status = "Available"
        else: "Borrowed"
        print("Title: ",book_title," | Author: ", author ," | Status: ",status, sep="'", end=".\n")

book1 = books()

while True:
    functions = int(input("\nplease enter the number of the function you'd like to use! \n 1 - add a book \n 2 - check for a book \n 3 - borrow \n 4 - return a book \n 5 - check an authors titles \n 6 - all books \n 0 - EXIT\n Enter : "))
    if functions == 1:
        add_book()
    elif functions == 2:
        checking()
    elif functions == 3:
        borrow()
    elif functions == 4:
        returning()
    elif functions == 5:
        search()
    elif functions == 6:
        library()
    elif functions == 0:
        print("\n\n\n thank you for using this mini-project! --Ali Essam\n\n\n")
        break
    else:
        print("invalid choice, try again!\n\n")
    