import sqlite3
import time
import datetime
import random


def create_table(dbInfo):
    """
    Create a table for our DB
    :param dbInfo: dbInfo
    :return: nothing
    """
    dbInfo['cur'].execute("""CREATE TABLE IF NOT EXISTS mock_data(
         id         INT,
         snumber    INT,
         sname      TEXT,
         city       TEXT,
         state      TEXT,
         postalCode TEXT,
         hprice     REAL)""")
    print("Done creating mock_data table")


def data_entry(dbInfo):
    """
    Manual data entry
    :param dbInfo: DB info dict
    :return: nothing
    """
    dbInfo['cur'].execute("""INSERT INTO STUFF
            VALUES(1234561679,
            '2017-12-14 10:11:30',
            'Python',
            5) """)
    # Commit to DB
    dbInfo['con'].commit()


def read_data(dbInfo):
    """
    Reads data from DB
    :param dbInfo:
    :return: nothing
    """
    dbInfo['cur'].execute("""SELECT * FROM STUFF
    WHERE value = 4""")
    data = dbInfo['cur'].fetchall()
    for row in data:
        print(row)

def dynamic_data_entry(dbInfo):
    """
    Dynamically enter information to table
    :param dbInfo: DB connection dict
    :return: nothing
    """
    unix = int(time.time())
    # datetime.datetime.fromtimestamp: takes a unix time
    # strtime: will convert to a string in any format
    date = datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")
    keyword = 'Python'
    value = random.randrange(0, 10) # random 0-10
    dbInfo['cur'].execute("""INSERT INTO STUFF
            (unix, datestamp, keyword, value)
            VALUES(?, ?, ?, ?)""",
            (unix, date, keyword, value))
    # Commit to DB
    dbInfo['con'].commit()


def delete_data(dbInfo):
    """
    Delete records
    :param dbInfo: DB info dict
    :return: nothing
    """
    print('Before deleting data')
    dbInfo['cur'].execute("""SELECT * FROM STUFF""")
    data = dbInfo['cur'].fetchall()
    [print(row) for row in data]

    # Delete data
    dbInfo['cur'].execute("""DELETE FROM STUFF
        WHERE value = 2""")

    print('After deleting data')
    dbInfo['cur'].execute("""SELECT * FROM STUFF""")
    data = dbInfo['cur'].fetchall()
    [print(row) for row in data]

def main():
    dbInfo = {} # db related info
    # Connect to DB
    dbInfo['con'] = sqlite3.connect('tutorial.db')
    # Create a cursor (interact with DB)
    dbInfo['cur'] = dbInfo['con'].cursor()
    # 1) Create a table
    #create_table(dbInfo)
    # 2) Insert data
    #data_entry(dbInfo)
    # for i in range(10):
    #     dynamic_data_entry(dbInfo)
    #     time.sleep(3)
    # 3) Read data
    #read_data(dbInfo)
    # 4) Delete data
    delete_data(dbInfo)

    # Clean
    dbInfo['cur'].close()
    dbInfo['con'].close()

if __name__ == '__main__':
    main()

