
class Library:
    book_list = []
    
    @classmethod   
    def entry_book(cls,book):
        cls.book_list.append(book)
    
    
    
class Book:
    def __init__(self,book_id,title,author,availability):
        self.__book_id = book_id
        self._title = title
        self.__author = author
        self.availability = availability
        Library.entry_book(self)

    
    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"\nBook '{self._title}' borrowed succesfully.")
            
        else:
            print(f"\nBook '{self.__title}' is already borrowed.")
    
    def return_book(self):
        if not self.availability:
            self.availability = True
            print(f"\nBook '{self._title}' returned succesfully.")
            
        else:
            print(f"\nBook '{self._title}' was not borrowed.")
            
            
    def view_book_info(self):
        availability_status = 'Available' if self.availability else "Not Available"
        print(f'Book Id : {self.__book_id}, Title : {self._title}, Author : {self.__author}, Availability : {availability_status}')
    
    def get_book_id(self):
        return self.__book_id
    
    
    
    
Book(1,'Python','Mahbub',True)
Book(2,'C++','Ratan',True)
Book(3,'Java','Samiul',True)
Book(4,'C','Arif',True)
Book(5,'C#','Azad',True)
Book(6,'Java Script','Rahat khan',True)




while(True):
    
    print('\n------------Library Menu------------')
    print('1. View all books')
    print('2. Borrow book')
    print('3. Return book')
    print('4. Exit')
    
    choice = int(input('Enter your choice : '))
    
    if choice == 1:
        print('\nLibrary books')
        for book in Library.book_list:
            book.view_book_info()
            
    elif choice == 2:
        book_id = int(input('Enter book ID to borrow : '))
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                book.borrow_book()
                break
        else:
            print('Invalid book ID')
            
    elif choice == 3:
        book_id = int(input('Enter book id for return : '))
        for book in Library.book_list:
            if book.get_book_id() == book_id:
                book.return_book()
                break
        else:
            print('Invalid book ID')
            
    elif choice == 4:
        print('\nThanks for using our Library')
        break
    
    else:
        print('\nInvalid choice. please choose again')
        