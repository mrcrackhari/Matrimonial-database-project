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
    SUM(m.annual_income) AS total_income,
    AVG(m.annual_income) AS average_income,
    MIN(m.annual_income) AS minimum_income,
    MAX(m.annual_income) AS maximum_income

FROM member_info m

INNER JOIN occupations o
    ON m.occupation = o.id

WHERE m.annual_income IS NOT NULL
  AND m.annual_income > 0

GROUP BY o.id, o.occupation_name

ORDER BY average_income DESC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_11_occupation_income_analysis.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Occupation",
        "Member Count",
        "Total Income",
        "Average Income",
        "Minimum Income",
        "Maximum Income"
    ])

    writer.writerows(data)

print("Report 11 CSV created successfully!")

cursor.close()
mydb.close()