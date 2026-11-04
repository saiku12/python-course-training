import keyword

# Part 2: Ask the user three questions
person_name = input("Enter your name: ")
goal_name = input("Enter one skill you want to get better at: ")
target_month = input("Enter the month you want to reach it by: ")

# Part 3: Store daily practice time
daily_minutes = 30

# Part 4: Print the heading
print("\nMY PERSONAL GOAL PLAN\n")

# Part 5: Print the goal plan
print("Name:", person_name)
print("Goal:", goal_name)
print("Target month:", target_month)
print("Daily practice:", daily_minutes, "minutes")

# Part 6: Print two lines using end=
print("Status:", end=" ")
print("Not started")

print("Reminder:", end=" - ")
print("Practise every day!")

# Part 7: Print the goal sentence
print("\nIn one sentence:")
print(person_name, "plans to work on", goal_name, "for", daily_minutes, "minutes every day until", target_month)

# Print Python's reserved keywords
print("\nWords Python has reserved for itself:\n")
print(keyword.kwlist)