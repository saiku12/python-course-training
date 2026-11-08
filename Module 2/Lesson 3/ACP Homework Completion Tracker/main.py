
# ================================
# HOMEWORK COMPLETION TRACKER
# ================================

print("===== HOMEWORK COMPLETION TRACKER =====")

# PART 1: Set the homework task count
total_homework = 4
original_count = total_homework

# PART 2: Create the counters
completed_count = 0
task_num = 1

# PART 3: While loop
while task_num <= total_homework:

    print("\nHomework Task", task_num)

    # PART 4: Choose the current task
    if task_num == 1:
        print("Task: Complete Python homework")

    elif task_num == 2:
        print("Task: Complete Mathematics homework")

    elif task_num == 3:
        print("Task: Complete Science homework")

    else:
        print("Task: Complete English homework")

    # PART 5: Check whether the task is completed
    answer = input("Is this task completed? (yes/no): ").lower()

    if answer == "yes":
        completed_count = completed_count + 1
        task_num = task_num + 1
        print("Great! Task completed.")

    else:
        print("Please complete this task before moving to the next one.")

    # PART 6: Show remaining homework
    remaining = total_homework - completed_count
    print("Remaining homework:", remaining)

# PART 7: Safe infinite loop example
print("\n===== SAFE INFINITE LOOP EXAMPLE =====")

safety_counter = 0

while True:
    print("This loop is running safely.")

    safety_counter = safety_counter + 1

    if safety_counter == 3:
        print("Stopping the loop using break.")
        break

# PART 8: Final summary
print("\n===== HOMEWORK COMPLETION SUMMARY =====")

print("Total homework tasks:", original_count)
print("Completed tasks:", completed_count)
print("Remaining tasks:", original_count - completed_count)

print("\nCongratulations! Homework tracker finished.")
