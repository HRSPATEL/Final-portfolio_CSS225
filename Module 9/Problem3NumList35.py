# Harsh Patel
# problem 3
# 12.05.2022

# Using a while loop, ask the user to enter a number. Append each entered number
# to a list and add them together. Continue asking for a number until the sum of the list of
# numbers is greater than 100.


H=[]
while(sum(H)<=100):
	n = int(input("Please enter number and press enter(until sum is 100) "))
	H.append(n)