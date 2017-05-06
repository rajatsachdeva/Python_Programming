#!/usr/bin/python3

# Databases in python
# Database used here is SQLite 3
# row factory in sqlite3

import sqlite3

def main():
    
    # Connects to database and creates the actual db file if not exits already
    db = sqlite3.connect('test.db')
    
    # this now creates a row object
    # which can be converted to a dictionary object
    db.row_factory = sqlite3.Row
    
    # Interact with the database
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values(?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values(?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values(?, ?)', ('three', 3))
    db.execute('insert into test (t1, i1) values(?, ?)', ('four', 4))
    # commit the changes in database
    db.commit()
    
    cursor = db.execute('select i1, t1 from test order by i1')
    # Data comes in Objects
    for row in cursor:
        print (row)
        print(dict(row))
        print(row['t1'], row['i1'])
    print()
           
if __name__ == "__main__": main()
