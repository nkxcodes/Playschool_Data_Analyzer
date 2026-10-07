
import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv('data/students.csv')
    
    total_number_of_students = df['Student'].count()
    number_of_students_in_each_class = df.groupby('Class')['Student'].count()
    average_age = df['Age'].mean()
    average_attendance = df['Attendance'].mean().round(2)
    average_activity_score = df['Activity_Score'].mean().round(2)
    highest_attendance = df['Attendance'].max()
    lowest_attendance = df['Attendance'].min()
    
    print()
    print(f'Total numbers of students: {total_number_of_students}')

    print()
    print('Number of students in each clas: ')
    print(number_of_students_in_each_class)

    print()
    print(f'Average age: {average_age}')

    print()
    print(f'Average attendance: {average_attendance}')

    print()
    print(f'Average activity score: {average_activity_score}')

    print()
    print(f'Highest attendance: {highest_attendance}')

    print()
    print(f'Lowest attendance: {lowest_attendance}')

    print()
    print(f'========== FEE ANALYSIS ==========')

    total_fees_collected = df['Fees_Paid'].sum()
    average_amount_paid_per_students = df['Fees_Paid'].mean()
    df['Fee_Due'] = df['Total_Fee'] - df['Fees_Paid']
    students_with_due_fees = df[df['Total_Fee'] != df['Fees_Paid']][['Student', 'Fee_Due']]
    total_outstanding_amount = df['Fee_Due'].sum()

    print()
    print(f'Total fees collected: {total_fees_collected}')

    print()
    print(f'Average amount paid per student: {average_amount_paid_per_students}')

    print()
    print("Students who haven't paid the full fee: ")
    print()
    print(students_with_due_fees)

    print()
    print(f'Total outstanding amount: ₹{total_outstanding_amount}')

    print()
    print('========== Attendance Analysis ==========')

    average_attendance_per_class = df.groupby('Class')['Attendance'].mean()
    class_with_highest_average_attendance = average_attendance_per_class.idxmax()
    class_with_lowest_average_attendance = average_attendance_per_class.idxmin()

    print()
    print('Average attendance per class: ')
    print()
    print(average_attendance_per_class)

    print()
    print(f'Class with highest average attendance: {class_with_highest_average_attendance}')

    print()
    print(f'Class with lowest average attendance: {class_with_lowest_average_attendance}')

    print()
    print('========== Visualization ==========')

    plt.subplot(2, 1, 1)
    x = number_of_students_in_each_class.index
    y = number_of_students_in_each_class.values

    plt.bar(x, y, color='purple')

    plt.subplot(2, 1, 2)
    x2 = average_attendance_per_class.index
    y2 = average_attendance_per_class.values
    
    plt.bar(x2, y2, color='green')
    plt.show()

    with open("report.txt", "w") as file:
        file.write("PLAYSCHOOL STUDENT REPORT\n")
        file.write("=========================\n\n")

        file.write(f"Total Students: {total_number_of_students}\n")
        file.write(f"Average Age: {average_age:.2f}\n")
        file.write(f"Average Attendance: {average_attendance}%\n")
        file.write(f"Average Activity Score: {average_activity_score:.2f}\n")
        file.write(f"Highest Attendance: {highest_attendance}%\n")
        file.write(f"Lowest Attendance: {lowest_attendance}%\n\n")

        file.write("STUDENTS IN EACH CLASS\n")
        file.write("----------------------\n")
        file.write(number_of_students_in_each_class.to_string())
        file.write("\n\n")

        file.write("FEE REPORT\n")
        file.write("----------\n")
        file.write(f"Total Fees Collected: ₹{df['Fees_Paid'].sum()}\n")
        file.write(f"Average Amount Paid Per Student: ₹{average_amount_paid_per_students:.2f}\n")
        file.write(f"Total Outstanding Amount: ₹{total_outstanding_amount}\n\n")

        file.write("STUDENTS WITH DUE FEES\n")
        file.write("----------------------\n")
        file.write(students_with_due_fees.to_string())
        file.write("\n\n")

        file.write("ATTENDANCE BY CLASS\n")
        file.write("-------------------\n")
        file.write(average_attendance_per_class.to_string())
        file.write("\n\n")

        file.write(f"Class With Highest Average Attendance: {class_with_highest_average_attendance}\n")
        file.write(f"Class With Lowest Average Attendance: {class_with_lowest_average_attendance}\n")


if __name__ == "__main__":
    main()
