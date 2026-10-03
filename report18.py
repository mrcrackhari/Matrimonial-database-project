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
    o.occupation_name,
    h.education,
    c.city_name,
    m.annual_income

FROM member_info m

INNER JOIN occupations o
    ON m.occupation = o.id

INNER JOIN highesteducation h
    ON m.highest_education = h.id

INNER JOIN city c
    ON m.city = c.id

WHERE m.annual_income > 400000
  AND o.occupation_name NOT IN ('Student', 'Unemployed')

ORDER BY m.annual_income DESC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_08_excluded_occupations.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "First Name",
        "Middle Name",
        "Last Name",
        "Occupation",
        "Education",
        "City",
        "Annual Income"
    ])

    writer.writerows(data)

print("Report 08 CSV created successfully!")

cursor.close()
mydb.close()