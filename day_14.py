
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price=price
    def display(self):
        print("Title: "+title)   
        print("Author: "+author)
        print("Price: "+str(price)) 
        

