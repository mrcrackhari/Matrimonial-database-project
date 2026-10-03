import mysql.connector
import csv


con =mysql.connector.connect(
           host="localhost",
           user="root",
           password="",
           database="matrimonial_website"
)

cursor = con.cursor(dictionary = True)

cursor.execute("""
        SELECT m.profile_code,m.first_name,m.middle_name,m.last_name,g.gender,c.city_name,o.occupation_name,h.education,m.annual_income FROM member_info m 
        INNER JOIN gender g ON m.gender = g.id
        INNER JOIN city c ON m.city = c.id
        INNER JOIN occupations o ON m.occupation = o.id
        INNER JOIN highesteducation h ON m.highest_education = h.id
        WHERE m.annual_income > 500000  ORDER BY m.annual_income DESC;


""")

data = cursor.fetchall()

with open("report_03_high_income.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[ "profile_code",
        "first_name",
        "middle_name",
        "last_name",
        "gender",
        "city_name",
        "occupation_name",
        "education",
        "annual_income"
        ]
    )

    writer.writeheader()
    writer.writerows(data)

print("Data exported successfully")

cursor.close()
con.close()