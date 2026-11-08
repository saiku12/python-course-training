
print("===== HOLIDAY ACTIVITY PLANNER =====")
print("Welcome to your Holiday Activity Planner!")

print("\nChoose your holiday type:")
print("1. Beach Holiday")
print("2. Mountain Holiday")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("\nYou selected Beach Holiday!")
    print("Choose your activity:")
    print("1. Swimming")
    print("2. Sandcastle Building")

    activity = int(input("Enter your activity choice (1 or 2): "))

    if activity == 1:
        print("\nActivity: Swimming")
        print("Enjoy swimming in the cool water!")
        print("Recommendation: Carry your swimsuit and sunscreen.")

    else:
        print("\nActivity: Sandcastle Building")
        print("Have fun building beautiful sandcastles!")
        print("Recommendation: Carry a bucket and spade.")

elif choice == 2:
    print("\nYou selected Mountain Holiday!")
    print("Choose your activity:")
    print("1. Hiking")
    print("2. Camping")

    activity = int(input("Enter your activity choice (1 or 2): "))

    if activity == 1:
        print("\nActivity: Hiking")
        print("Enjoy exploring the beautiful mountain trails!")
        print("Recommendation: Wear comfortable shoes.")

    else:
        print("\nActivity: Camping")
        print("Enjoy a wonderful night under the stars!")
        print("Recommendation: Carry a tent and sleeping bag.")

else:
    print("\nInvalid choice!")
    print("Please select 1 or 2.")

print("\nThank you for using the Holiday Activity Planner!")
print("Have a wonderful holiday!")
