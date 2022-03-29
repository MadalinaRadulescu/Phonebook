name = input("What's your name?: ")
print("Hello " + name + ", I am your phone book")

age = int(input("How old are you?:"))
if age <= 18:
    print("You are so young! Life is ahead of you!")
elif age > 18 and age < 40:
    print("That's a nice age!")
elif age > 40:
    print("You must be very wise!")
elif isinstance(age,int) == False:
    print("That doesn't seem to be an integer.")





# "How old are you?"
# - "You are so young! Life is ahead of you!"
# - "That's a nice age!"
# - "You must be very wise!"
# - "That doesn't seem to be an integer."
