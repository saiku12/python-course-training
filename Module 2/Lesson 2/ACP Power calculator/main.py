
# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# PART 1: Ask for base and exponent
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

# PART 2: Create the running total
result = 1

# PART 3 + 4: Multiply using a for loop
for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, ": result =", result)

# PART 5: Print the final answer
print("\nAnswer:", base, "to the power", exponent, "=", result)
