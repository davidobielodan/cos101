
title = "Weekly Expense Tracker For Students"

# Display title in uppercase
print(title.upper())

# INPUT
name = input("What is your full name? ")

print("-----------------------------------")
print("Hello " + name + ", this program will enable you to track your weekly expenses.")
print("-----------------------------------")

# INPUTS
# int() is used because the assignment requires whole-naira inputs.

dailyTransportCost = int(input("Enter your daily transport cost: "))
dailyFeedingCost = int(input("Enter your daily feeding cost: "))
numberOfDaysOnCampus = int(input("How long have you stayed on campus in days? "))
extraExpenses = int(input("Enter your other expenses for the week: "))
weeklyBudget = int(input("Enter your weekly budget: "))


# VALIDATION
# Reject negative expense values, days and budget.

if dailyTransportCost < 0 or dailyFeedingCost < 0 or numberOfDaysOnCampus < 0 or extraExpenses < 0 or weeklyBudget < 0:

    print("-----------------------------------")
    print("ERROR: Negative values are not allowed.")
    print("Please enter valid positive values or zero.")

else:

    # PROCESSES
    transportTotal = dailyTransportCost * numberOfDaysOnCampus
    feedingTotal = dailyFeedingCost * numberOfDaysOnCampus

    weeklyTotal = transportTotal + feedingTotal + extraExpenses

    # BUDGET COMPARISON
    if weeklyTotal < weeklyBudget:
        budgetStatus = "Within budget"
        amount = weeklyBudget - weeklyTotal
        message = "Amount remaining: NGN" + str(amount)

    elif weeklyTotal == weeklyBudget:
        budgetStatus = "Exactly on budget"
        message = "No amount remaining."

    else:
        budgetStatus = "Over budget"
        amount = weeklyTotal - weeklyBudget
        message = "Amount exceeded: NGN" + str(amount)

    # OUTPUT
    print("")
    print("WEEKLY EXPENSE SUMMARY")
    print("-----------------------------------")
    print("STUDENT: " + name.upper())

    print("TOTAL TRANSPORT FOR " + str(numberOfDaysOnCampus) + " DAYS: NGN" + str(transportTotal))
    print("TOTAL FEEDING FOR " + str(numberOfDaysOnCampus) + " DAYS: NGN" + str(feedingTotal))
    print("OTHER EXPENSES: NGN" + str(extraExpenses))
    print("WEEKLY TOTAL: NGN" + str(weeklyTotal))

    print("-----------------------------------")
    print("WEEKLY BUDGET: NGN" + str(weeklyBudget))
    print("BUDGET STATUS: " + budgetStatus)
    print(message)
    print("-----------------------------------")
