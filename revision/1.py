input1 = int(input("Enter the first value of lcm: "))
input2 = int(input("Enter the second value of lcm: "))

# Function to calculate the HCF (Greatest Common Divisor)
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a

# Calculate LCM using the formula: LCM(a, b) = abs(a * b) / HCF(a, b)
lcm = abs(input1 * input2) // hcf(input1, input2)

print(f"The LCM is: {lcm}")
