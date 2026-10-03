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
    m.profile_code,
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

WHERE m.annual_income > 500000

ORDER BY m.annual_income DESC

LIMIT 10
"""

cursor.execute(query)

data = cursor.fetchall()

with open("report_04_top_10_income.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Profile Code",
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

print("Report 04 CSV created successfully!")

cursor.close()
mydb.close()