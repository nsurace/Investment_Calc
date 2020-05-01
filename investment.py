'''
Program: investment.py
Autho:Nick
Date: 4/28/2020
page 276
'''

from breezypythongui import EasyFrame

class Investment(EasyFrame):
	'''An investment calculator that demosnstrates the use of a multiline text area'''
	def __init__(self):
		'''Sets up the window and widgets'''
		EasyFrame.__init__(self, title = "Investment Calculator")
		#Labels for the window
		self.addLabel(text = "Initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0)
		
		#Entry fields
		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addIntegerField(value = 0, row = 2, column = 1)

		#Button
		self.compute = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)

		#Text area widget
		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)

	#Event handling methods
	def compute(self):
		'''Computes the investment schedule based on the inputs and outputs the schedule in the text area'''
		#Obtain and validate the inputs
		startBalance = self.amount.getNumber()
		rate = self.rate.getNumber()/100
		years = self.period.getNumber()
		if startBalance == 0 or rate == 0 or years == 0:
			return #this gets you out of the function

		#Set the header for the table
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")

		#Compute and append the results for each year
		totalInterest = 0.0
		for year in range(1, years + 1):
			interest = startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		#Append	the totals for the period
		result += "Ending balance: $%0.2f\n" % endBalance
		result += "Total interest earned: $%0.2f\n" % totalInterest

		#Output the result whil preserving read only status
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

def main():
	'''Instantiates and pops up the window'''
	Investment().mainloop()		

#Global call to main() function
main()
