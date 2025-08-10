# Working with tuples (immutable sequences)

colors = ("red", "green", "blue")
print("Tuple:", colors)

# Access elements
print("First color:", colors[0])

# Tuples can't be changed, but can be concatenated
new_colors = colors + ("yellow",)
print("New tuple:", new_colors)