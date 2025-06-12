# Welcome to your main.py file.
# This is where you will write code throughout the course.
# You will get a fresh main.py file for each exercise.

# Python allows you to import code from other files in the same directory.
# Each main.py file will import some code from "game_mechanics.py".
# game_mechanics.py contains the code that will use your code to run the game.
# You should not edit game_mechanics.py.
# All the code you need from game_mechanics.py will already be imported for you.
from game_mechanics import HiddenNumber


# This is a python variable. It's used to store numbers, strings, lists, etc.
# This variable is used to set the exercise number for the hidden number game.
# You will need to change this variable to move to the next exercise.
exercise_number = 0

# This uses code from game_mechanics to create your hidden number game for each exercise.
hidden_num = HiddenNumber(exercise_number=exercise_number)

# Run this code to try out the hidden number game for the first exercise!


# P.S. if you get stuck, you can uncomment this line to see a hint. Try
# not to use it unless you have to!
# hidden_num.hint()
