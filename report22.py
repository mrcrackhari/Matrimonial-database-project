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
    o.occupation_name,
    COUNT(m.profile_code) AS member_count,
    AVG(m.annual_income) AS average_income

FROM member_info m

INNER JOIN occupations o
    ON m.occupation = o.id

WHERE m.annual_income IS NOT NULL
  AND m.annual_income > 0

GROUP BY o.id, o.occupation_name

HAVING AVG(m.annual_income) >= 500000

ORDER BY average_income DESC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_12_high_income_occupations.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Occupation",
        "Member Count",
        "Average Income"
    ])

    writer.writerows(data)

print("Report 12 CSV created successfully!")

cursor.close()
mydb.close()