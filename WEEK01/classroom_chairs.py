# A program to calcutae and display the total number of chairs in a classroom from a fixed arrangement of rows an columns
# 8 chairs per row = 8 columns

#INPUTS
rows = 6
columns = 8
print("")
print("There are " + str(rows) + " rows of chairs, and " + str(columns) + " chairs per row [COLUMNS]")


#PROCESS
totalChairs = rows * columns

#OUTPUT
print("TOTAL NUMBER OF CHAIRS IN THE CLASS: " + str(totalChairs) + " CHAIRS")

