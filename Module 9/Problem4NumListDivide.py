# Harsh Patel
# problem 4
# 12.05.2022

# Create a while loop that initializes a counter at 0 and will run until the counter
# reaches 50. If the value of the counter is divisible by 10, append the value to the list called tens.
# Confirm the list results using a print statement

i = 0
tens = []
while(i <= 50):
    if i % 10 == 0:
        tens.append(i)
    i = i + 1

print("the list of tens until 50", tens)