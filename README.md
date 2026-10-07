# Playschool Student Data Analyzer

I built this project to practice using Python, Pandas, and Matplotlib on a small playschool student dataset.

The idea was simple: take student data from a CSV file, analyze it, create some visualizations, and generate a basic report.

## What it does

The program analyzes things like:

* Total number of students
* Number of students in each class
* Average age
* Average attendance
* Highest and lowest attendance
* Average activity score
* Students with unpaid fees
* Total fees collected
* Total outstanding fees
* Average attendance for each class
* Class with the highest average attendance
* Class with the lowest average attendance

It also creates charts to make some of the results easier to understand.

## Tools I used

* Python
* Pandas
* Matplotlib
* CSV
* Basic file handling

## Project structure

```text
playschool_data_analyzer/
│
├── data/
│   └── students.csv
│
├── analyzer.py
│
├── report.txt
│
└── README.md
```

## How it works

The program reads the student data from `students.csv`.

Then Pandas is used to calculate different statistics and find useful information from the data.

Matplotlib is used to visualize some of the results.

Finally, the important results are saved into `report.txt`.

So the basic flow is:

```text
students.csv
     ↓
   Pandas
     ↓
 Data Analysis
     ↓
 Matplotlib
     ↓
  Report
```

## What I learned

This project helped me understand how different Python tools can work together instead of learning them separately.

I practiced:

* Reading CSV files with Pandas
* Selecting columns
* Using `groupby()`
* Calculating `mean()`, `sum()`, `max()` and `min()`
* Filtering rows
* Creating new columns
* Using `.index` and `.values` for visualization
* Creating bar charts with Matplotlib
* Writing analysis results to a text file
* Organizing a small Python project

## Note

The student data used in this project is **sample/fake data** created for learning purposes. It does not contain real student information.

## What I want to improve later

This is my first project, so there are still many things I can improve.

Some possible improvements are:

* Make the report more detailed
* Add more useful visualizations
* Improve the project structure
* Add better error handling
* Allow the user to provide their own CSV file
* Automate more of the reporting process

This project is mainly about learning and getting comfortable with building something from start to finish.