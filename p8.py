def bmi_calculator():
    print("--- BMI Calculator ---")
    choice = input("Choose units: (1) Metric (kg/m) or (2) Imperial (lb/in): ")

    if choice == '1':
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))
    elif choice == '2':
        weight_lbs = float(input("Enter weight in lbs: "))
        height_in = float(input("Enter height in inches: "))
        # Convert to metric
        weight = weight_lbs * 0.453592
        height = height_in * 0.0254
    else:
        print("Invalid choice.")
        return

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Interpret results
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Interpretation: {category}")

bmi_calculator()
