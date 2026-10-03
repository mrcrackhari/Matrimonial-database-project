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
    h.education,
    o.occupation_name,
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

WHERE g.gender = 'Female'
  AND m.annual_income > 500000
  AND (c.city_name = 'Mumbai' OR c.city_name = 'Pune')

ORDER BY m.annual_income DESC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_07_female_high_income_city.csv",
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
        "Education",
        "Occupation",
        "Annual Income"
    ])

    writer.writerows(data)

print("Report 07 CSV created successfully!")

cursor.close()
mydb.close()