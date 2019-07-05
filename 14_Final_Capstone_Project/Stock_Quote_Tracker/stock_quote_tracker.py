# <summary>
# Udemy course - Complete Python Bootcamp
# Section 14: Final Capstone Python Project
# Stock Ticker Tracker
# </summary>

from yahoo_fin.stock_info import *

menu = 0
stock_list = ['MSFT','SYMC','GOOG','FB','AMZN','NFLX','GOOGL']

class Stock():
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = get_quote_table(ticker,True)
        self.price = get_live_price(ticker)
        self.open = self.data['Open']
        self.perc_change = (self.price-self.open)/100.0

    def __str__(self):
        return str(self.ticker)+"\t"+str(round(self.price,2))+"\t"+str(round(self.open,2))+"\t"+str(round(self.perc_change,2))

    def update(self, ticker):
        self.data = get_quote_table(ticker,True)
        self.price = get_live_price(ticker)
        self.open = self.data['Open']
        self.perc_change = (self.price-self.open)/100.0

class Portfolio():
    def __init__(self):
        self.portfolio = []
        for ticker in stock_list:
            self.portfolio.append(Stock(ticker))

    def __str__(self):
        portfolio_comp = ''
        for stock in self.portfolio:
            portfolio_comp += '\n'+ stock.__str__()
        return "Ticker\tPrice\tOpen\t% Change\n"+portfolio_comp

    def update(self):
        for stock in self.portfolio:
            stock.update(stock.ticker)

    def add(self,ticker):
        self.portfolio.append(Stock(ticker))

    def remove(self,ticker):
        for index, stock in enumerate(self.portfolio):
            if stock.ticker == ticker:
                break
        self.portfolio.pop(index)

def add_symbol(portfolio,symb):
    try:
        portfolio.add(symb)
    except:
        print("Are you sure that is a valid ticker symbol?")

def rem_symbol(portfolio,symb):
    portfolio.remove(symb)

def show_prices(portfolio):
    portfolio.update()
    print("Current prices:")
    print(portfolio)

print("Welcome to the stock ticker program in Python!\nPlease wait while loading...\n")
portfolio = Portfolio()

while (menu != 4):
    print("Menu:\n1) Update and show current stock prices")
    print("2) Add symbol to tracked stocks")
    print("3) Remove symbol from tracked stocks")
    print("4) Quit program")
    menu = int(input("Please choose an option:  "))
    if menu == 1:
        print("\nLoading....\n")
        show_prices(portfolio)
        continue
    if menu == 2:
        symbol = (input("Please enter ticker symbol to add: ")).upper()
        add_symbol(portfolio,symbol)
        continue
    if menu == 3:
        symbol = (input("Please enter ticker symbol to remove: ")).upper()
        rem_symbol(portfolio,symbol)
        continue
    if menu == 4:
        print("\nThank you for using this program and have a nice day!\n")
        break
