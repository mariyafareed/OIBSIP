def calculate_bmi(weight_kg, height_m):#"calculat bmi given weight in kgs and height in meters"
    
    bmi = weight_kg / (height_m ** 2)
    return bmi
def interpret_bmi(bmi):
    #interprets BMI value and provide corressponding category
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def main():
    weight_kg = float(input("enter your weight in kilogrms:"))
    height_m = float(input("enter your height in meters:"))

    bmi = calculate_bmi(weight_kg, height_m)
    category = interpret_bmi(bmi)

    print("Your BMI id {bmi:.2f}, which is classified as {category}.")
    
if __name__ == "__main__":
    main()    