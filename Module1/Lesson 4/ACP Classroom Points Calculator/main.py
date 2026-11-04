# ================================
# CLASSROOM POINTS CALCULATOR
# ================================

# Step 1: Store team points
team1 = 120
team2 = 150
team3 = 100
team4 = 180
team5 = 150

# Step 2: Calculate total and average
total_points = team1 + team2 + team3 + team4 + team5
average_points = total_points / 5

print("Total points:", total_points)
print("Average points:", average_points)

# Step 3: Calculate reward stars
stars_per_point = 2
total_stars = total_points * stars_per_point

print("Total reward stars:", total_stars)

# Step 4: Calculate full boxes and leftover stars
box_size = 25
full_boxes = total_stars // box_size
leftover_stars = total_stars % box_size

print("Full boxes:", full_boxes)
print("Leftover stars:", leftover_stars)

# Step 5: Compare with last week's points
last_week = 1300

print("This week is greater than last week:", total_points > last_week)
print("This week is equal to last week:", total_points == last_week)
print("This week is greater than or equal to last week:", total_points >= last_week)

# Step 6: Update the total
total_points += 100
print("After bonus points:", total_points)

total_points -= 50
print("After missed-task penalty:", total_points)