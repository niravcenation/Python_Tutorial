# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# BMI = Weight / (height*height)

#Write your code below this line 👇
BMI = float(weight) / (float(height)*float(height))
print(int(BMI))