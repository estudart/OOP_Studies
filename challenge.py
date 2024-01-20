# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: use inheritance and abstract classes

# Challenge: create a class structure to represent stocks and bonds
# Requirements:
# -- Both stocks and bonds have a price
# -- Stocks have a company name and ticker
# -- Bonds have a description, duration, and yield
# -- You should not be able to instantiate the base class
# -- Subclasses are required to override get_description()
# -- get_description returns formats for stocks and bonds
# For stocks: "Ticker: Company -- $Price"
# For bonds: "description: duration'yr' : $price : yieldamt%"

from abc import ABC, abstractmethod

class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

class Stock(Asset):
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.company = company
        self.ticker = ticker

    def get_description(self):
        return f"{self.ticker}: {self.company} -- {self.price}"
    
    def __lt__(self, value):
        return self.price < value.price
    
    def __str__(self):
        return f"{self.company}, ${self.price}"

class Bond(Asset):
    def __init__(self, price, description, duration, bond_yield):
        super().__init__(price)
        self.description = description
        self.duration = duration
        self.bond_yield = bond_yield

    def get_description(self):
        return f"{self.description}: {self.duration}yr : ${self.price} : {self.bond_yield}%"

    def __lt__(self, value):
        return self.bond_yield < value.bond_yield
    
    def __str__(self):
        return f"{self.description}, {self.bond_yield}%"

# ~~~~~~~~~ TEST CODE ~~~~~~~~~
# ~~~~~~~~~ TEST CODE ~~~~~~~~~
stocks = [
    Stock("MSFT", 342.0, "Microsoft Corp"),
    Stock("GOOG", 135.0, "Google Inc"),
    Stock("META", 275.0, "Meta Platforms Inc"),
    Stock("AMZN", 120.0, "Amazon Inc")
]

bonds = [
    Bond(95.31, "30 Year US Treasury", 30, 4.38),
    Bond(96.70, "10 Year US Treasury", 10, 4.28),
    Bond(98.65, "5 Year US Treasury", 5, 4.43),
    Bond(99.57, "2 Year US Treasury", 2, 4.98)
]

stocks.sort()
bonds.sort()

for stock in stocks:
    print(stock)
print("-----------")
for bond in bonds:
    print(bond)