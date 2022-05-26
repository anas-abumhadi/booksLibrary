import datetime

import Book
import Borrowing_order
import Librarian
import client

clients = []
librarians = []
books = []
borrowed_orders = []


def main():
    c = client.Client(200, "Ziad Morjan", 20, 200, 1234567)
    clients.append(c)

    l = Librarian.Librarian(100, "Anas Abu Mhadi", 20, 100, "full")
    librarians.append(l)

    b1 = Book.Book(301, "Python", "Book about Python", "aa", "inactive")
    books.append(b1)
    b2 = Book.Book(302, "C++", "Book about C++", "bb", "active")
    books.append(b2)
    b3 = Book.Book(303, "Java", "Book about Java", "cc", "active")
    books.append(b3)

    bookFlag = False
    statusFlag = False
    clintFlag = False
    tempBookId = int(input("Enter the book id you want to borrow : "))
    for book in books:
        if book.id == tempBookId:
            bookFlag = True
            if book.status == "active":
                statusFlag = True
                tempClintId = int(input("Enter your id : "))
                for clint in clients:
                    if clint.id == tempClintId:
                        clintFlag = True
                        br = Borrowing_order. Borrowing_order(400, datetime.datetime.now(), tempClintId, tempBookId, "active")
                        borrowed_orders.append(br)
                        book.status = "inactive"
                        print("The book has been borrowed successfully")

    if not bookFlag:
        print("The book is not found")
    else:
        if not statusFlag:
            print("The book is not available to borrow")
        else:
            if not clintFlag:
                print("The clint is not found")
#anas

main()
