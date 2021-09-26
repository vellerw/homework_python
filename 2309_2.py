books = ['Agatha Christie' , 'Fahrenheit 451' , 'Banana murder']
class Reader():
    books = []

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def take_book(self, book):
        if len(self.books) < 2:
            self.books.append(book)
        else:
            print('Too much')

    def return_book(self, book):
        if book in self.books:
            self.books.remove(book)


r = Reader('Bob', 'Makle', 15)
r.take_book('Red star')
r.take_book('Coffee book')
r.take_book('Sirius')
print(r.books)

