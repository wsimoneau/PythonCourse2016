import random
random.seed(25)

class Portfolio(object): #Create the class of the portfolio
	def __init__(self): 
		self.Cash = [] # Create a list for all of the cash transactions
		self.Stock = {} # Create a dictionary for all stock entries
		self.MutualFund = {} # Create a dictionary for all MF entries
		self.history = {} # Create a dictionary for the history entries
	def addCash(self, value): # Under the portfolio class I add a function to add cash to the cash list
		self.Cash.append(value) # Add all cash value added to the Cash in the portfolio
		print "Cash Total of %s Added." % value # To track entries running of this function will produce this string with the value for the entry logged.
		#self.history.append(Cash.log) # This was an attempt at creating the entry for history.  I excluded it since I was unable to get the function together.
	def buyStock(self, quantity, quote): # Create a function to add a quantity of a particular stock.
		self.Stock[quote.quote] = quantity # The addition to the Stock dictionary in portfolio. The quote.quote is pulling the quote from the Stock class. The dictionary entry will be this quote and the quantity requested.
		self.Cash.append(-(quantity * quote.price)) # As stock is purchased a debit to the Cash account will be made. The debit is the amount of stock and the price.
		print """
		%d Shares of %s Have Been Acquired \n
		and %d USD Debited from Cash Account
		""" % (quantity, quote.quote,(quantity * quote.price)) #This is the notice of the amount of which stock has been purchased, and the amount debited to the cash account.
	def buyMutualFund(self, amount, fund): #function to buy mutual fund
		self.MutualFund[fund.name] = amount # add to the mutual fund dictionary with the fund and amount of the fund
		self.Cash.append(-(amount)) # This registers the debit to the Cash account
		print """
		%d Shares of %s Fund Acquired \n
		and %d USD debited from Cash Account
		""" % (amount, fund.name, amount) # Prints the results of the transaction to the mutual fund dictionary and the cash list
	def withdrawCash(self, total): # create a function to withdraw cash
		self.Cash.append(-(total)) # The function will debit the cash account the amount withdrawn
		print "%d USD has been debited from your cash account." % total # Acknowledges the amount withdrawn from the cash account.
	def sellStock(self, quote, quantity):# Creates a function to sell Stock, which will be a reduction of the stock quantity and a debit to the cash account
		self.Stock[quote] -= quantity # This will reduce the stock dictionary of the quantity and stock input
		self.Cash.append(quote.price * random.uniform(.5,1.5)) #Add the value of the shares sold to the cash account
		print """
		%d Shares of %s sold at %d USD a share \n
		and %d USD credited to Cash Account.
		""" % (quantity, quote, random.uniform(.5,1.5), 5 * random.uniform(.5,1.5)) # Acknowledge the transactions to the user for the stock and the cash accounts
	def sellMutualFund(self, fund, amount): # Create a function to sell shares of the mutual fund
		self.MutualFund[fund] -= amount # Debits the shares sold from the mutual fund dictionary for the specified fund
		self.Cash.append(amount * random.uniform(.9, 1.2)) # Add the value of the mutual fund sold to the cash account
		print """
		%d Shares of %s Sold \n
		and %d USD credited to your Cash account
		""" % (amount, fund, amount * random.uniform(.9, 1.2)) #Lets the user know the amount of which fund has been sold and how much has been credited to the cash account
	def __repr__(self): #creates the function for the Portfolio class
		return "Portfolio ()"
	def __str__(self): # creates the string when the portfolio is printed
		return """
				Portfolio Value:\n
    			\n
    			Cash Total: $ %s \n
    			Stock Holdings: %r \n
    			Mutual Fund Assets: %r \n 
    			""" % ("%.2f" % sum(portfolio.Cash), portfolio.Stock, portfolio.MutualFund)
# The return function is returning the values that have been populated in the portfolio dictionaries and lists.
class Stock():# creates the class of Stock
	def __init__(self, price, quote): #Adds the necessary arguments for the class
		self.price = price # assigns the input for price into the type class
		self.quote = quote # assigns the input for quote into the type class
		print "%s at %d USD a Share" % (quote, price) # Lets the user know the input of the stock
		
class MutualFund(): # creates the mutual fund class
	def __init__(self, name): #Adds the necessary arguments for the class
		self.name = name # assigns the input for name into the class
		print "Mutual Fund - %s ." % name # Lets the user know that the mutual fund has been created

s = Stock(20, "HFH") # creates the stock "HFH" at a cost of 20
 

mf1 = MutualFund("BRT") #Creates BRT mutual fund
mf2 = MutualFund("GHT")	#Creates GHT mutual fund
			

portfolio = Portfolio()#creates the object of the portfolio class

portfolio.addCash(300.50) # Adds 300.50 to the portfolio

portfolio.buyStock(5, s) # buys 5 shares of the object s which was created

portfolio.buyMutualFund(10.3, mf1)# buys 10.3 shares of BRT mutual fund

portfolio.buyMutualFund(2, mf2) # buys 2 shares of GHT mutual fund

portfolio.withdrawCash(50) # Withdraw 50 dollars cash

portfolio.sellStock("HFH", 1) # sell 1 share of HFH stock

portfolio.sellMutualFund("BRT", 3) # sells 3 shares of BRT mutual fund




print(portfolio) # Prints the results of the all of the entries made into the portfolio

	
    
    








