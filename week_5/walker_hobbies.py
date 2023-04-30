
#  Title: walker-hobbies.py
#  Author: Megan Walker
#  Date: 04/15/23
#  Description: walker-hobbies.py for Web 335 Assign_5
#  References: WEB 335 GitHub, & WEB 335 Assign_5, provided by Professor Krasso

# Create a list of hobbies
hobbies = ["reading", "painting", "home projects", "cooking", "gardening","spending time with family"]

# Create a list of days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Print the hobbies list using a for loop
for hobby in hobbies:
    print(hobby)

# Print the days of the week list using a for loop
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Off today! Go enjoy hobbies!")
    else:
        print(f"{day}: It is a work day.")
