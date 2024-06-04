import os

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "\033[94m"  # Blue color
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "\033[92m"  # Green color
    elif 25 <= bmi < 29.9:
        return "Overweight", "\033[93m"  # Yellow color
    else:
        return "Obesity", "\033[91m"  # Red color

def save_bmi_history(bmi, category):
    with open("bmi_history.txt", "a") as file:
        file.write(f"BMI: {bmi:.2f}, Category: {category}\n")

def display_bmi_history():
    if os.path.exists("bmi_history.txt"):
        print("\nYour BMI History:")
        with open("bmi_history.txt", "r") as file:
            history = file.readlines()
            for entry in history:
                print(entry.strip())
    else:
        print("\nNo BMI history found.")

def main():
    print("Welcome to the BMI Calculator")
    
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            height = float(input("Enter your height in meters: "))
            
            if weight <= 0 or height <= 0:
                print("Weight and height must be positive values. Please try again.")
                continue
            
            bmi = calculate_bmi(weight, height)
            category, color = classify_bmi(bmi)
            
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"{color}Your BMI category is: {category}\033[0m")
            
            save_bmi_history(bmi, category)
            
            display_bmi_history()
            
            break
        
        except ValueError:
            print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
