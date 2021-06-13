# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrate how Pickling and Structured error handling work
#
# ChangeLog (Who,When,What):
# PBirkeland,06/12/2021,Created and started script
# PBirkeland,06/12/2021,Added code to complete assignmment 7
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
import pickle  # Allows you to pickle and store more complex data in a file

print("We are about to create the Pickling lists")
input("Please press the [Enter] key to continue.\n")

print("Pickling lists.\n")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("We are about to read a Pickle list from a file.")
input("Please press the [Enter] key to continue.")

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()

print("\nWe are about to attempt to open a file which does not exist.")
print("We have a try/except condition that will display a targetted error message.")
input("Please press the [Enter] key to continue.\n")

try:
    f = open('file.txt', 'r')
except:
    print('file does not exist')

input("\n\nPress the [Enter] key to exit.")

