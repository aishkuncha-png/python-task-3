marks = int(input("Enter your marks: "))

# Validate marks
if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

else:
    # Grade calculation
    if marks >= 90:
        grade = "A"
        print("Grade: A")

        # Nested condition
        if marks >= 95:
            print("Excellent performance! You are a top scorer.")

    elif marks >= 75:
        grade = "B"
        print("Grade: B")
        print("Very good performance.")

    elif marks >= 60:
        grade = "C"
        print("Grade: C")
        print("Good, but you can improve.")

    elif marks >= 40:
        grade = "D"
        print("Grade: D")
        print("You passed, but improvement is needed.")

    else:
        grade = "Fail"
        print("Grade: Fail")
        print("You need to work harder. Better luck next time!")
