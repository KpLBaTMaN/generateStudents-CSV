import csv
import names
from faker import Faker
import datetime

import random

numberOfStudents = 100


fake = Faker()
fake2 = Faker()
start_DOB_date = datetime.date(year=1996, month=1, day=1)
end_DOB_date = datetime.date(year=1999, month=1, day=1)

adding_number_date = [15, 30]


with open('Student.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["StudentID", "StudentName", "DOB",
                     "Address", "StudentType", "Data_of_Start"])

    for i in range(1, numberOfStudents):

        DOB = fake.date_between(start_DOB_date, end_DOB_date)
        Address = fake.address()
        StudentType = "Full Time"

        choice_number = random.randint(0, len(adding_number_date) - 1)

        date_of_start = datetime.date(
            year=(2015 + random.randint(0, 3)), month=6, day=adding_number_date[choice_number])

        Date_of_Start = date_of_start

        row = [i, names.get_full_name(), DOB,
               Address, StudentType, Date_of_Start]

        writer.writerow(row)
