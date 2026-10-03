import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="matrimonial_website"
)

cursor = mydb.cursor()

query = """
SELECT
    m.first_name,
    m.middle_name,
    m.last_name,
    g.gender,
    c.city_name,
    o.occupation_name,
    h.education,
    m.annual_income

FROM member_info m

INNER JOIN gender g
    ON m.gender = g.id

INNER JOIN city c
    ON m.city = c.id

INNER JOIN occupations o
    ON m.occupation = o.id

INNER JOIN highesteducation h
    ON m.highest_education = h.id

WHERE m.annual_income < 300000

ORDER BY m.annual_income ASC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_06_low_income_members.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "First Name",
        "Middle Name",
        "Last Name",
        "Gender",
        "City",
        "Occupation",
        "Education",
        "Annual Income"
    ])

    writer.writerows(data)

print("Report 06 CSV created successfully!")

cursor.close()
mydb.close()