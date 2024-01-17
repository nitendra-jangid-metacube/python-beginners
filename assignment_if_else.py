# Input marks for each subject
maths = int(input("Enter marks for Maths: "))
physics = int(input("Enter marks for Physics: "))
chemistry = int(input("Enter marks for Chemistry: "))

# Check if the student has passed in all three subjects
if maths >= 35 and physics >= 35 and chemistry >= 35:
    # Calculate average marks
    average = (maths + physics + chemistry) / 3
    
    # Grading based on average marks
    if average <= 59:
        grade = "C"
    elif average <= 69:
        grade = "B"
    else:
        grade = "A"
    
    print("Average marks: {:.2f}".format(average))
    print("Grade: {}".format(grade))
else:
    print("Failed in one or more subjects")
    print("Grade: F")