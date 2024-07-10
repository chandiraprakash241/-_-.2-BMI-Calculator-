def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) given weight and height.

    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: Calculated BMI
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """
    Determine the BMI category given a BMI value.

    Parameters:
    bmi (float): The calculated BMI value

    Returns:
    str: The BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
