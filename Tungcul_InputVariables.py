name = input("Name:")
course = input("Course (BSIT/BSCS/BSDA):")
year_level = int(input("Year Level(1/2/3): "))

print("Input the grade for the following courses:")

grades = []
grades.append(int(input("Input grade for CC1:")))
grades.append(int(input("Input grade for CC2:")))
grades.append(int(input("Input grade for CC7:")))

average_grade = (grades[0] + grades[1] + grades[2]) / 3

print(f"Hello {name} of {course}-{year_level}. Here are your grades and average:")

print("CC1 Grade:",grades[0])
print("CC2 Grade:",grades[1])
print("CC7 Grade:",grades[2])
print("Average:", average_grade)




