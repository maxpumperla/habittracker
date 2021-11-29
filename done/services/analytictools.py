import sqlite3
import pandas as pd


# Query the database and return all records
def returnAllHabits():
    # connect to database
    conn = sqlite3.connect('habittracker.db')
    # create a cursor
    c = conn.cursor()

    # Query the database
    c.execute("SELECT rowid, * FROM habits")
    data = c.fetchall()

    df = pd.DataFrame(data, columns=['Nr', 'Name', 'Periodicity', 'Start Date',
                                     'Last Checked', 'Current Streak',
                                     'Longest Streak'])
    df_no_indices = df.to_string(index=False)

    print(df_no_indices)

    # comit our connection
    conn.commit()
    # close our connection
    conn.close()

# return all Habits that are currently Tracked
# def returnCurrentlyTrackedHabits():


# return habit with longest streak
def returnLongestStreak(name):
    # connect to database
    conn = sqlite3.connect('habittracker.db')
    # create a cursor
    c = conn.cursor()

    # fetch all streaks from the database
    c.execute("SELECT longest_streak FROM habits WHERE name =:n", {"n": name})
    s = c.fetchone()
    given_streak = s[0]

    print(f"The longest streak of {name} was: {given_streak}")

    # comit our connection
    conn.commit()
    # close our connection
    conn.close()


def returnGivenStreak(name):
    # connect to database
    conn = sqlite3.connect('habittracker.db')
    # create a cursor
    c = conn.cursor()

    # fetch the streak from the database where the name is the name wrote
    c.execute("SELECT streak FROM habits WHERE name =:n", {"n": name})
    s = c.fetchone()
    given_streak = s[0]

    print(name, "has the streak:", given_streak)

    # comit our connection
    conn.commit()
    # close our connection
    conn.close()


def returnHabitSamePeridocity(periodicity):
    # connect to database
    conn = sqlite3.connect('habittracker.db')
    # create a cursor
    c = conn.cursor()

    # fetch the streak from the database where the periodicity is
    # the number we specified
    c.execute("SELECT name,periodicity FROM habits WHERE periodicity =:p",
              {"p": periodicity})
    data = c.fetchall()

    df = pd.DataFrame(data, columns=['Name', 'Periodicity'])
    df_no_indices = df.to_string(index=False)

    print(df_no_indices)

    # commit our connection
    conn.commit()
    # close our connection
    conn.close()
