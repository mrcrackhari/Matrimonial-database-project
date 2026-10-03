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
    c.city_name,
    AVG(m.annual_income) AS average_income

FROM member_info m

INNER JOIN city c
    ON m.city = c.id

WHERE m.annual_income IS NOT NULL
  AND m.annual_income > 0

GROUP BY c.id, c.city_name

ORDER BY average_income DESC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_10_city_average_income.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "City",
        "Average Income"
    ])

    writer.writerows(data)

print("Report 10 CSV created successfully!")

cursor.close()
mydb.close()