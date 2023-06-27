class Library:
    dict = {"Sapiens": "library", "RdPd": "library", "random": "library"}

    @classmethod
    def display(cls):
        print("Here is the list of books")
        for n in Library.dict.keys():
            print(n)

    @classmethod
    def add(cls):
        m = input("Enter book name.")
        n = "library"
        Library.dict[m] = n
        print("Book added successfully")

    @classmethod
    def lend(cls):
        m = input("Enter book name which you want to lend.")
        n = input("Enter the person name who want book.")
        if Library.dict.get(m):
            Library.dict[m] = n
        else:
            print("Book does not exists in our library")
        print("Book lent successfully")

    @classmethod
    def return_book(cls):
        Library.add()
        print("Book returned successfully")


def run():
    while (5):
        x = int(input("Enter\n 1 to add book\n 2 to display books\n 3 to lend book\n 4 to return book\n 0 to quit"))
        if x == 1:
            Library.add()
        elif x == 2:
            Library.display()
        elif x == 3:
            Library.lend()
        elif x == 4:
            Library.return_book()
        elif x == 0:
            quit()
        else:
            print("enter the correct input from the given list")
            run()

def main():
    run()
main()