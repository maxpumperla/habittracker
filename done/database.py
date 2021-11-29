import sqlite3

# connect to database
conn = sqlite3.connect('habittracker.db')

# create a cursor
c = conn.cursor()

# create a table
c.execute('''CREATE TABLE habits (
        name string,
        periodicity integer,
        start_date string,
        last_checked string,
        streak integer,
        longest_streak integer,
        UNIQUE(name)
    )''')

# commit our command
conn.commit()

# close our connection
conn.close()
