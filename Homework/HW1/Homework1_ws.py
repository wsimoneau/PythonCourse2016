import random
random.seed(25)

class Portfolio(object):
	def __init__(self):
		self.Cash = []
		self.Stock = {}
		self.MutualFund = {}
		self.history = {}
	def addCash(self, value):
		self.Cash.append(value)
		print "Cash Total of %s Added." % value
		#self.history.append(Cash.log)
	def buyStock(self, quantity, quote):
		self.Stock[quote.quote] = quantity
		self.Cash.append(-(quantity * quote.price))
		print """
		%d Shares of %s Have Been Acquired \n
		and %d USD Debited from Cash Account
		""" % (quantity, quote.quote,(quantity * quote.price))
	def buyMutualFund(self, amount, fund):
		self.MutualFund[fund.name] = amount
		self.Cash.append(-(amount))
		print """
		%d Shares of %s Fund Acquired \n
		and %d USD debited from Cash Account
		""" % (amount, fund.name, amount)
	def withdrawCash(self, total):
		self.Cash.append(-(total))
		print "%d USD has been debited from your cash account." % total
	def sellStock(self, quote, quantity):
		self.Stock[quote] -= quantity
		#self.Cash.append(quote.price * random.uniform(.5,1.5))
		print """
		%d Shares of %s sold at %d USD a share \n
		and %d USD credited to Cash Account.
		""" % (quantity, quote, random.uniform(.5,1.5), 5 * random.uniform(.5,1.5))
	def sellMutualFund(self, fund, amount):
		self.MutualFund[fund] -= amount
		self.Cash.append(amount * random.uniform(.9, 1.2))
		print """
		%d Shares of %s Sold \n
		and %d USD credited to your Cash account
		""" % (amount, fund, amount * random.uniform(.9, 1.2))
	def __repr__(self):
		return "Portfolio ()"
	def __str__(self):
		return """
				Portfolio Value:\n
    			\n
    			Cash Total: $ %s \n
    			Stock Holdings: %r \n
    			Mutual Fund Assets: %r \n 
    			""" % ("%.2f" % sum(portfolio.Cash), portfolio.Stock, portfolio.MutualFund)

class Stock():
	def __init__(self, price, quote):
		self.price = price
		self.quote = quote
		print "%s at %d USD a Share" % (quote, price)
		
class MutualFund():
	def __init__(self, name):
		self.name = name
		print "Mutual Fund - %s ." % name

s = Stock(20, "HFH")
 

mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
			

portfolio = Portfolio()

portfolio.addCash(300.50)

portfolio.buyStock(5, s)

portfolio.buyMutualFund(10.3, mf1)

portfolio.buyMutualFund(2, mf2)

portfolio.withdrawCash(50)

portfolio.sellStock("HFH", 1)

portfolio.sellMutualFund("BRT", 3)




print(portfolio)

	
    
    








