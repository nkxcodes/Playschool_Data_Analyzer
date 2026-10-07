
import pandas as pd

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
    print('Number of studnets in each clas: ')
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

    total_fees_collected = df['Total_Fee'].sum()
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

if __name__ == "__main__":
    main()
