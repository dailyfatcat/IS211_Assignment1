
class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    
    def display(self):
        print(self.title + " written by " + self.author)
        
if __name__ == "__main__":
    obj1 = Book('John Steinbeck', 'Of Mice and Men')
    obj1.display()
    obj2 = Book('Harper Lee', 'To Kill a Mockingbird')
    obj2.display()
