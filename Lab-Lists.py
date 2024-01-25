# Create 3 lists and fill them with student information—one with name values, one with hometown
# values, one with favorite food values.
# Prompt the user to ask about a particular student by number. Convert the input to an integer.
# Use the integer as the index for the lists. Print the student’s name
# ask user to display hometown or favorite food and display relevant information
# Ask the user if they would like to learn about another student.
# Validate user number: Use an if statement to check if the number is out of range, i.e. either less
# than 1 or greater than the length of the lists. If so, display a friendly message and let the user try again
# Ask the user what information category to display: "Hometown" or "Favorite Food".
# Use an if statement to check that they entered either category name correctly.
# If they entered an incorrect category, display a friendly message and re-ask the question. (See hints below!)
# Use the first list’s length property in your code instead of hardcoding it.
# Provide an option where the user can see a list of all students.
# Allow the user to search by student name (Good challenge but difficult!)
# Category names: Allow uppercase and lowercase; allow portion of word such as "Food" instead of "Favorite Food"

name = ['Frank', 'Sally', 'Carlos']
hometown = ['Charlotte', 'Yonkers', 'Jamaica']
favorite_food = ["Pizza", "Hamburgers", "Pasta"]
choice = True
while choice:
    see_all = input("would you like to see a list off all students? y/n ")
    if see_all == "y":
        print(name)
    stu_name = input("enter student name you would like to learn more about ").capitalize()
    for n in name:
        if n == stu_name:
            print(stu_name + " is in student directory!")
    user_inp = int(input("enter the students number 1-3 ")) - 1
    while user_inp > len(name) or user_inp < 0:
        print("invalid input try again!")
        user_inp = int(input("enter the students number 1-3 ")) - 1
    print(name[user_inp])
    home_or_fav = input("enter (hometown) or (favorite food) to learn more about them ")
    while home_or_fav != 'hometown' and home_or_fav != "favorite food":
        print("not a valid option! try again ")
        home_or_fav = input("Would you like to learn about their hometown or favorite food? ")
    if home_or_fav == "hometown":
        print(hometown[user_inp])
    elif home_or_fav == "favorite food":
        print(favorite_food[user_inp])
    else:
        print("not a valid option! try again ")
    ask = input("Would you like to learn about another student? y/n ")
    if ask == "n":
        choice = False
    elif ask == 'y':
        choice = True
