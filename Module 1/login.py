# login.py

# Harsh Patel
# 10/04/2022

# The program only allows certain username, and it is case-sensitive.
# For Jack it says, Access granted
# For Jill it says, Welcome to the system
# I added my name, which says, Welcome NLU student

username = input("Login: >> ")
user1 = "Jack"
user2 = "Jill"
user3 = "Harsh"
if username == user1:
    print("Access granted")
elif username == user2:
    print("Welcome to the system")
elif username == user3:
    print("Welcome NLU student")
else:
    print("Access denied")
