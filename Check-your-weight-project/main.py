weight = int(input("Enter your weight: "))
unit = input("(L)bs or (K)g: ")

if unit.lower() == 'k':
    ans = weight / 0.453592  # Convert kilograms to pounds
else:
    ans = weight * 0.453592  # Convert pounds to kilograms

print(ans)
