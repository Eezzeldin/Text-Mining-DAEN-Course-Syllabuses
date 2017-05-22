import sqlite3

conn = sqlite3.connect ('DEAN.sqlite')
cur  = conn.cursor ()
cur.execute (''' DROP TABLE IF EXISTS Courses''')
cur.execute ('''CREATE TABLE IF NOT EXIST Courses  (CourseTitle VARCHAR , CourseURL VARCHAR , Coursedesc VARCHAR)''')
for i in range (134):
    Title = courses [i]
    url   = urls [i]
    Desc  = coursedec [i]
    cur.execute (''' INSERT INTO Courses (CourseTitle,CourseURL,Coursedesc) VALUES (?,?,?)''', (Title,url,Desc))
cur.commit()
cur.close ()
