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
SELECT DISTINCT
    m.first_name,
    m.middle_name,
    m.last_name,
    m.date_of_birth,
    c.city_name

FROM member_info m

INNER JOIN city c
    ON m.city = c.id

ORDER BY
    m.first_name,
    m.middle_name,
    m.last_name,
    m.date_of_birth,
    c.city_name
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_27_unique_name_dob_city.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "First Name",
        "Middle Name",
        "Last Name",
        "Date of Birth",
        "City"
    ])

    writer.writerows(data)

print("Report 21 CSV created successfully!")

cursor.close()
mydb.close()

