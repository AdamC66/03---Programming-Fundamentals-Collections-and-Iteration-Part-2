# Exercise 9
# We're going to make a shopping list by storing a few items in a list. Feel free to start with whatever items you like:
# grocery_list = ["carrots", "toilet paper", "apples", "salmon"]
# After each step, run your program to ensure it works before you move onto the next one. It's a good idea to commit often, too.

grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

# Your next step should present your grocery list with an item on each line, with an asterisk (*) in front of it so that it appears like this:
def display_list(list):
    for item in list:
        print(f"* {item}")

# You realize you've forgotten some rice, so add it to your list and output it again. Given that you've already output your list twice, it might be good to consider writing a method to do this. Putting frequently used chunks of code in a method lets you reuse them throughout your program without having to type them out over and over.
grocery_list.append("rice")
# You lost count of how many things you need to pick up. Better output the total number of items on your list.
print(len(grocery_list))

# Check to see if your list includes "bananas". If it does, output "You need to pick up bananas". Otherwise, output "You don't need to pick up bananas today".
if "bananas" not in grocery_list:
    print("You need to pick up bananas")
    grocery_list.append("bananas")
else:
    print("You don't need to pick up bananas today")

# Display the second item in the list. (Don't forget that lists indices start at zero!)
print(grocery_list[1])

# It turns out that everything in this grocery store you're visiting is stored alphabetically, so to better plan out what you need to buy you should sort your grocery list and output it with asterisks again.
grocery_list.sort()

# After looking everywhere, you can't find the salmon. Delete it from your list and redisplay the list one last time.
grocery_list.remove("salmon")

display_list(grocery_list)

# After you're done, be sure you have everything committed and pushed to your github repo.

print("\n\n\n")
# Exercise 10
# Start out by creating the following dictionary representing the number of students in past Bitmaker cohorts:

students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

# Create a method that displays the name and number of students for each cohort, like so:

def display_cohorts(students):
    for name,size in students.items():
        print(f"{name}: {size} students")
    print("")
display_cohorts(students)
# Add cohort 4, which had 43 students, to the dictionary.
students['cohort4'] =43
display_cohorts(students)
# Use the keys method to output all of the cohort names.
print(students.keys())
# The classrooms have been expanded! Increase each cohort size by 5% and display the new results.

for name, size in students.items():
    students[name] = int(size*1.05) #made this an int after multiplying because you cant have a fraction of a student
display_cohorts(students)
# Delete the 2nd cohort and redisplay the dictionary.
del students["cohort2"]
display_cohorts(students)

# BONUS: Calculate the total number of students across all cohorts using a for loop. Output the result.
totalstudents = 0
for name, size in students.items():
    totalstudents += size
print(totalstudents)