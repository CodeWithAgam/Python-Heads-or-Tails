# The below function prints Heads or Tails using the random module
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Using the random module to generate a random number
import random

# Use the randint command to get a random number between 0 and 1
randomInt = random.randint(0, 1)

# If random number is 1 then print Heads, otherwise print Tails
if randomInt == 1:
    print("Heads")

else:
    print("Tails")