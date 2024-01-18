class Book:
    count = 1

    def __init__(self, title: str, author: str, pages: int, price: float):
        self.code = Book.count
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret"
        Book.count+=1

    def get_price(self):
        if hasattr(self, "_discount"):
            self.price = self.price - (self.price * self._discount)
            return self.price
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount



b1 = Book('Peace and War', 'Erico', 257, 100)
print(b1.get_price())
b2 = Book('Brave New Book', 'Erico', 257, 100)
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())
print(b2._Book__secret)
print(b2.code)