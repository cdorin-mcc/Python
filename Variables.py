"""Create a Python program that converts kilograms to pounds. Use at least four different samples to convert. A sample of the math is provided below; do not use the same example in your program."""
# Conversion factor
kg_to_lbs = 2.20462
# Samples in kilograms
kg_examples = [7.5, 19.01, 21, 30]
# Converted Results in pounds
for kg in kg_examples:
    lbs = kg * kg_to_lbs
    print(f"{kg} kg is equal to {lbs:.2f} lbs");
