# ================================
# STUDENT APP ACCESS MANAGER
# ================================

# Step 1: Create permission constants
CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8

# Step 2: Create app lists
approved_apps = ["coding app", "math app", "science app"]
restricted_apps = ["gaming app", "social media app"]

# Step 3: Collect student input
student_name = input("Enter your name: ")
requested_app = input("Enter the app you want to use: ").lower()

# Step 4: Identity operators
print("\n--- Identity Checks ---")
print("Student name is a string:", type(student_name) is str)
print("Requested app is not an integer:", type(requested_app) is not int)

# Step 5: Membership operators
print("\n--- App Checks ---")
print("App is approved:", requested_app in approved_apps)
print("App is not restricted:", requested_app not in restricted_apps)

# Step 6: Combine permission bits using OR
student_permissions = CAMERA | MICROPHONE | STORAGE

print("\n--- Permission Details ---")
print("Permission value:", student_permissions)
print("Binary value:", bin(student_permissions))

# Step 7: Check individual permissions using AND
print("Camera enabled:", (student_permissions & CAMERA) != 0)
print("Microphone enabled:", (student_permissions & MICROPHONE) != 0)
print("Storage enabled:", (student_permissions & STORAGE) != 0)
print("Location enabled:", (student_permissions & LOCATION) != 0)

# Step 8: Demonstrate bit shifts
print("\n--- Bit Shifts ---")
print("Camera shifted left:", CAMERA << 1)
print("Storage shifted right:", STORAGE >> 1)

# Step 9: Final access result
print("\n--- Access Result ---")

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", student_name, "for", requested_app)
else:
    print("Access denied to", student_name, "for", requested_app)