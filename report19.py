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
    h.education,
    COUNT(m.profile_code) AS member_count

FROM member_info m

INNER JOIN highesteducation h
    ON m.highest_education = h.id

GROUP BY h.id, h.education

ORDER BY member_count DESC
"""

cursor.execute(query)

data = cursor.fetchall()

with open(
    "report_09_education_member_count.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Education",
        "Member Count"
    ])

    writer.writerows(data)

print("Report 09 CSV created successfully!")

cursor.close()
mydb.close()