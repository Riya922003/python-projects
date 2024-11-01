# Pattern 1: Square Pattern
for i in range(4):
    for j in range(4):  # Use 'j' as the inner loop variable
        print("# ", end="")  # Print '#' without a newline

    print()  # Move to the next line after each row

print("Using Pattern 1")
print("")  # Print a blank line for spacing

# Pattern 2: Right-Angled Triangle (Left-Aligned)
print("Using Pattern 1")
for i in range(4):
    for j in range(i + 1):  # Print increasing number of '#'
        print("# ", end="")

    print()  # Move to the next line after each row

print("Using Pattern 2")
# Pattern 3: Inverted Right-Angled Triangle
for i in range(4):
    for j in range(4 - i):  # Print decreasing number of '#'
        print("# ", end="")

    print()  # Move to the next line after each row
