# You are going to write a program that calculates the average student height from a List of heights.
#
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# Important You should not use the sum() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.


student_heights = input("Input a list of student heights :").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
for students in student_heights:
    sum = sum + students

average = sum / (n + 1)
print(round(average))