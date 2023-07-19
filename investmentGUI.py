"""
Program: investmentGUI.py
Author: Nikko Kapetanos 7/14/2023

GUI-based version of the investment calculator app from Chapter 3. Also illustrates the use of the Text Area component

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""

from breezypythongui import EasyFrame

# Other imports go here

# Class header (application name will change project to project)
class TextAreaDemo(EasyFrame):
	# Definition of our class constructor method
	def __init__(self):
		EasyFrame.__init__(self, title = "Investment Calculator")
		# Create and add the components to the window
		self.addLabel(text = "Initial Amount", row = 0, column = 0)
		self.addLabel(text = "Number of Years", row = 1, column = 0)
		self.addLabel(text = "Interest Rate in %", row = 2, column = 0)

		self.amount = self.addFloatField(value = 0.0, row = 0, column = 1)
		self.period = self.addIntegerField(value = 0, row = 1, column = 1)
		self.rate = self.addFloatField(value = 0.0, row = 2, column = 1)

		self.compute = self.addButton(text = "Compute", row = 3, column = 0,columnspan = 2,command = self.compute )
		self.compute["background"] = "yellow"
		self.compute["foreground"] = "red"

		self.outputArea = self.addTextArea(text = "", row = 4, column = 0, columnspan = 2, width = 50, height = 15)
	# Definition of the compute() function
	def compute(self):
		# Obtain and validate the inputs
		startBalance = 	self.amount.getNumber()
		years = self.period.getNumber()
		rate = self.rate.getNumber() / 100

		if startBalance == 0 or years == 0 or rate == 0:
			return

		# Initialize the accumulator variable for the interest over time 
		totalInterest = 0.0

		# Dispaly the header in tabular format for the output
		result = "%4s%18s%10s%16s\n" % ("Year", "Starting Balance", "Interest", "Ending Balance")

		# Compute and append the results for each year
		for year in range(1, years + 1):
			interest =  startBalance * rate
			endBalance = startBalance + interest
			result += "%4d%18.2f%10.2f%16.2f\n" % (year, startBalance, interest, endBalance)
			startBalance = endBalance
			totalInterest += interest

		# Append the totals for the entire investment period
		result += "Ending balance: $%0.2f\n" % endBalance 
		reult += "Total interest earned: $%0.2f\n" % totalInterest

		# Output the final result
		self.outputArea["state"] = "normal"
		self.outputArea.setText(result)
		self.outputArea["state"] = "disabled"

		

# Global definition of the main() method
def main():
	# instantiate an object from the class into mainloop()
	TextAreaDemo().mainloop()

# Global call to the main() for program entry
if __name__ == '__main__':
	main()