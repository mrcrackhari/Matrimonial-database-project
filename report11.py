import mysql.connector
import csv

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="matrimonial_website"
)

mycursor = mydb.cursor()


mycursor.execute("""
    SELECT 
    m.profile_code,
    m.first_name,
    m.middle_name,
    m.last_name,
    c.city_name AS city,
    d.district_name AS district,
    s.state_name AS state,
    g.gender AS gender,
    ms.status AS marital_status
    FROM member_info m
    INNER JOIN city c ON m.city= c.id
    INNER JOIN district d ON m.district = d.id
    INNER JOIN state s ON m.state = s.id
    INNER JOIN gender g ON m.gender = g.id
    INNER JOIN marital_status ms ON m.marital_status = ms.id
    WHERE ms.status = 'Never Married'  
    ORDER BY m.first_name ASC, m.last_name ASC;
    """)

data = mycursor.fetchall()

with open("report_01_active_members_name_asc.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)
    writer.writerow([
         "profile_code",
        "first_name",
        "middle_name",
        "last_name",
        "city",
        "district",
        "state",
        "gender",
        "marital_status"
       
    ])


    for row in data:
        writer.writerow(row)

print("Data exported successfully")


mycursor.close()
mydb.close()