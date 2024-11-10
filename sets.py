# Create an empty set
s = set()

# Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

# Print the set
print(s) # No elements appear twice in a set

# Remove elements from the set
s.remove(3)
print(s) #  3 is removed & only 1,2,4 are printed

# Length of the set
print(f"The set has {len(s)} elements.")
print(len(s))