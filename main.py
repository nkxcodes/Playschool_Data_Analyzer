
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

if __name__ == "__main__":
    main()
