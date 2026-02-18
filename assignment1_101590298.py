"""
Author: Dheeraj
Assignment: #1
Student ID : Dheeraj
"""

# Step 1: Variables

gym_member = "Sophie Miller"       # str
preferred_weight_kg = 42.5         # float
highest_reps = 30                  # int
membership_active = False          # bool


# Step 2: Dictionary
# workout_stats is of type dict[str, tuple[int, int, int]]
# Tuple represents (Yoga, Running, Weightlifting) minutes
workout_stats = {
    "Daniel": (35, 40, 30),
    "Priya": (50, 45, 35),
    "Lucas": (20, 60, 25)
}


# Step 3: Calculate total workout minutes and add new keys

for friend in list(workout_stats.keys()):
    total_minutes = sum(workout_stats[friend])
    workout_stats[friend + "_Total"] = total_minutes


# Step 4: Create 2D nested list
# workout_list is of type list[list[int]]
workout_list = []

for value in workout_stats.values():
    if isinstance(value, tuple):
        workout_list.append(list(value))


# Slice 1: Extract Yoga and Running minutes for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and Running minutes for all friends:", yoga_running)


# Slice 2: Extract Weightlifting minutes for last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)


# Step 5: Check for total workout >= 120 minutes

for key, value in workout_stats.items():
    if "_Total" in key and value >= 120:
        name = key.replace("_Total", "")
        print(f"Great job staying active, {name}!")


# Step 6: User Input Feature

friend_name = input("Enter friend's name: ")

if friend_name in workout_stats and isinstance(workout_stats[friend_name], tuple):
    yoga, running, weightlifting = workout_stats[friend_name]
    total = workout_stats[friend_name + "_Total"]
    
    print(f"\nWorkout summary for {friend_name}:")
    print("Yoga minutes:", yoga)
    print("Running minutes:", running)
    print("Weightlifting minutes:", weightlifting)
    print("Total workout minutes:", total)
else:
    print(f"Friend {friend_name} not found in the records.")


# Step 7: Highest and Lowest Total Workout Minutes

totals = {}

for key in workout_stats:
    if "_Total" in key:
        totals[key] = workout_stats[key]

highest = max(totals, key=totals.get)
lowest = min(totals, key=totals.get)

print("\nFriend with highest total workout minutes:",
      highest.replace("_Total", ""),
      f"({totals[highest]} minutes)")

print("Friend with lowest total workout minutes:",
      lowest.replace("_Total", ""),
      f"({totals[lowest]} minutes)")
     
     
      # final submission  version