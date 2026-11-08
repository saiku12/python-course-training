
# ================================
# LOOP ART DESIGNER
# ================================

print("===== LOOP ART DESIGNER =====")


# ---------- PART 1: STAR PYRAMID ----------
print("\n===== STAR PYRAMID =====")

rows = int(input("Enter the number of rows for Star Pyramid: "))

# ---------- PART 2: Build rows and columns ----------
for i in range(1, rows + 1):

    for j in range(i):
        print("* ", end="")

    print()


# ---------- PART 3: FLOYD'S TRIANGLE ----------
print("\n===== FLOYD'S TRIANGLE =====")

rows = int(input("Enter the number of rows for Floyd's Triangle: "))

number = 1

# ---------- PART 4: Print increasing numbers ----------
for i in range(1, rows + 1):

    for j in range(i):
        print(number, end=" ")
        number += 1

    print()


# ---------- PART 5: NUMBER DIAMOND ----------
print("\n===== NUMBER DIAMOND =====")

diamond_rows = int(input("Enter the number of rows for Diamond: "))

# Calculate half rows
if diamond_rows % 2 == 0:
    half_rows = diamond_rows // 2
else:
    half_rows = (diamond_rows // 2) + 1


# ---------- PART 6: UPPER HALF OF DIAMOND ----------
for i in range(1, half_rows + 1):

    # Print leading spaces
    for j in range(half_rows - i):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, 2 * i):
        print(j, end=" ")

    print()


# ---------- PART 7: LOWER HALF OF DIAMOND ----------
for i in range(half_rows - 1, 0, -1):

    # Print leading spaces
    for j in range(half_rows - i):
        print(" ", end=" ")

    # Print numbers
    for j in range(1, 2 * i):
        print(j, end=" ")

    print()


# ---------- PART 8: FINAL MESSAGE ----------
print("\n===== PATTERN DESIGN COMPLETED =====")
print("Thank you for using Loop Art Designer!")
