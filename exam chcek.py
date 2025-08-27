reason = input ("Do you have medical reason: (yes/no):").lower()
if reason == "yes":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 60:
        print("you are eligible for exam.")
    else:
        print("you are not eligible for exam.") 
     
elif reason == "no":
    attendence = int(input("Enter your attendence percentage: "))
    if attendence >= 75:
        print("you are eligible for exam.")
    else:
        print("you are not eligible for exam.")
else:
    print("Invalid input! please choose fron yes or no.")
