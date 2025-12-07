import pandas as pd

student_dicts = {
    "Name" : ["Aaditya", "Ankit", "Rohan", "Rahul"],
    "IQ" : [100, 90, 80, 120],
    "Marks" : [90, 80, 70, 95],
    "Package" : [10, 12, 7, 15]
}

students = pd.DataFrame(student_dicts)
students  





ipl = pd.read_csv("/home/aaditya/Desktop/Python/Pandas/ipl-matches.csv")
movies = pd.read_csv("/home/aaditya/Desktop/Python/Pandas/movies.csv")
batsman_run = pd.read_csv("/home/aaditya/Desktop/Python/Pandas/batsman_runs_ipl.csv")