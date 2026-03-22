# =========================
# Week Homework
# =========================

# -------------------------
# Part 0 – Write Your Name
# -------------------------

# TODO: Write your name inside the quotes
student_name="Jensen"

print(student_name)


input()
# -------------------------
# Part 1 – Multiple Choice
# -------------------------

# Write your answers below.
# Example: answer1 = "A"

# TODO: Write your answer for Question 1
answer1 = "B"

# TODO: Write your answer for Question 2
answer2 = "A"

# TODO: Write your answer for Question 3
answer3 = "B"

print("Your answers:")
print("Q1:", answer1)
print("Q2:", answer2)
print("Q3:", answer3)

# -------------------------
# Part 2 – Coding Task
# Dice Game
# -------------------------

import random

# TODO: Create a variable to store the dice roll
roll = 0

# TODO: Use a while loop so the game continues while the number is not 6
while roll !=6:

    # TODO: Generate a random number between 1 and 6
    num = random.randint(1,6) 

    # TODO: Print the dice number
    print(num)

    # TODO: If the number is 6, print "Jackpot!"
    if num == 6:
        print("Jackpot!")
    