# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = float(weight) / (float(height)*float(height))
print(int(BMI))
