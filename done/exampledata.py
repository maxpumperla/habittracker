import sqlite3
from datetime import date


# connect to database
conn = sqlite3.connect('habittracker.db')
# create a cursor
c = conn.cursor()


many_habits = [
               ('Sport', 7, date(2021, 11, 2), date(2021, 11, 23), 5, 5),
               ('Yoga', 7, date(2021, 11, 2), date(2021, 11, 20), 1, 4),
               ('Make_the_bed', 1, date(2021, 11, 2), date(2021, 11, 24), 1, 9),
               ("Stretch", 1, date(2021, 11, 2), date(2021, 11, 25), 13, 13),
               ("Read_a_book", 7, date(2021, 11, 2), date(2021, 11, 21), 1, 3)
 ]
# Query the database
c.executemany("INSERT OR IGNORE INTO habits VALUES (?,?,?,?,?,?)", many_habits)

print("Command executed succesfully...")
# comit our connection
conn.commit()

# close our connection
conn.close()
