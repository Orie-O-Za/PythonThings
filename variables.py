#
# Example file for variables
#

# Declare a variable and initialize it
f=0
print(f)

# Re-declaring the variable works
f = "abc"
print(f)

# ERROR: Variables of different types cannont be combined
print("This is a string " + str(123))

# Global vs. local variables in functionscdef
def someFunction():
    f="def"
    print(f)

someFunction()
print(f)