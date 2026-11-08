title = "Weekly Expense Tracker For Students"
#this is because strings are immutable which means they do not change
print(title.upper())
#INPUT : NAME input method returns vales in strings by default, a string
#would be necessary for concatenation with othe strings and strings
#can't be used to perform mathematical expressions
name = input("What is your full name? ")

print("-----------------------------------")
print("Hello "+ name + " this program would enable you to track your weekly expense provided all the necessary questions are answered correctly")
print("-----------------------------------")

#INPUTS floats used to convert a string to a decimal number used because
#numbers containing decimal values may be inputted by the student for
#the required variables: dailyTransportCost and dailyFeedingCost int
#used to convert a string to a whole number or interger
dailyTransportCost = float(input("Enter your daily transport cost "))
dailyFeedingCost = float(input("Enter your daily Feeding cost "))
#int used in this case because conventionally days are represented as whole number / intergers [numbers without decimal]
numberOfDaysOnCampus = int(input("How long have you stayed on campus in days? "))
extraExpenses = float(input("Enter your other expenses for the week "))


#PROCESSES
transportTotal = dailyTransportCost * numberOfDaysOnCampus
feedingTotal = dailyFeedingCost * numberOfDaysOnCampus
weeklyTotal = transportTotal + feedingTotal + extraExpenses

#LINE BREAK
print("")

#OUTPUT
print("WEEKLY EXPENSE SUMMARY")
print("-----------------------------------")
print("STUDENT: " + name.upper())

#floats are displayed in 1 decimal place by default so
#f"{variable:.2f}": Used to convert floats to 2 decimal places

#str used to convert a numerical value to a string
#str was used in this case because a string cannot be concatenated with a numerical value: floats and intergers
print("TOTAL TRANSPORT FOR " + str(numberOfDaysOnCampus)  + " DAYS: " + "NGN" + str(f"{transportTotal:.2f}"))
print("TOTAL FEEDING FOR " + str(numberOfDaysOnCampus) + " DAYS: " + "NGN" + str(f"{feedingTotal:.2f}"))
print("OTHER EXPENSES: " + "NGN" + str(f"{extraExpenses:.2f}"))
print("WEEKLY TOTAL: " + "NGN" + str(f"{weeklyTotal:.2f}"))



