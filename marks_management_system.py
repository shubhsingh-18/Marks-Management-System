print("======================================")
print("          Student Information")
print("======================================")


def vit_student(registration_no, name_student):
    return {
        "registration_no": registration_no,
        "name": name_student
    }
fresherstudents = []

cat1_marks={}

while True:
    print("\n.   Enter Student Details.     ")

    reg_no = input("Enter Registration Number: ").strip().upper()
    if reg_no == "0":
        break

    studentname = input("Enter Student Name: ").strip()
    fresherstudents.append(vit_student(reg_no, studentname))

    print("\nEnter Marks for", studentname)
    problem_solving = float(input("introduction to Problem Solving: "))
    electric_circuits = float(input("Electric Circuits and System: "))
    calculus = float(input("calculus: "))
       
    cat1_marks[reg_no] = {
        "introduction to problem solving": problem_solving,
        "electric circuits and system": electric_circuits,
        "calculus": calculus
    }
    print("\nStudent added successfully!")

    more = input("\nDo you want to add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break

print("\n=========================================================")
print("                   Student Result")
print("=========================================================")
print("\nEnter the registration number of the student you want to see. ")

while True:
    register_no = input("\nEnter registration number: ").strip().upper()

    if register_no == "0":
        print("Program ended.")
        break

    found = False

    for student in fresherstudents:
        if student["registration_no"].upper() == register_no:
            print("\n--- Student Found ---")
            print("Registration No:", student["registration_no"])
            print("Name:", student["name"])
            print("\n--- Marks ---")

            print("Problem Solving:",
                  cat1_marks[reg_no]["introduction to problem solving"])

            print("Electric Circuits and System:",
                  cat1_marks[register_no]["electric circuits and system"])

            print("calculus:",
                  cat1_marks[register_no]["calculus"])
           
            total_marks = (
                cat1_marks[register_no]["introduction to problem solving"]
                + cat1_marks[register_no]["electric circuits and system"]
                + cat1_marks[register_no]["calculus"])
           
            average_marks = total_marks / 3
            average_markscat1 = round(average_marks, 2)
         
            if average_markscat1 >= 90:
                grade = "S"

            elif average_markscat1 >= 80:
                grade = "B"

            elif average_markscat1 >= 70:
                grade = "C"

            elif average_markscat1 >= 60:
                grade = "D"

            elif average_markscat1 >= 50:
                grade = "E"

            else:
                grade = "F"
        
            if average_markscat1 >= 40:
             qualification = "PASS \n"
             "CONGRATULATION YOU ARE PROMOTED \n"
             "THANK YOU! "
            else:
             qualification = "FAIL \n " 
             "BETTER LUCK NEXT TIME \n" 
             "THANK YOU"

            print("\n-------- Result ---------")
            print("Total Marks:", total_marks)
            print("Average Marks:", average_marks)
            print("Grade:", grade)
            print("Result:", qualification)

            found = True

            continue_search = input("\nDo you want to see the result of another student? (yes/no): ").strip().lower()
            if continue_search != "yes":
                print("TO EXIT THE LOOP TYPE 0.")
                break

    if not found:
        print("\nStudent not found.")

        retry = input("Do you want to search again? (yes/no): ").strip().lower()
        if retry != "yes":
            break
