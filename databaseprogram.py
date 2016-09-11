# Programs for database

import sqlite3
testconnection=sqlite3.connect("Modelprograms.db")
"""table=testconnection.execute("select * from studentdata")
output=testconnection.execute("select branch from studentdata where name='sindhu'")
print table.fetchall()
print output.fetchone()"""

#newtable=testconnection.execute("alter table Employeedata alter column 'Employeename' text")
testconnection.execute('insert into Employeedata(EmployeeID,Department) values(1256,"HR")')
testconnection.commit()
view=testconnection.execute("select * from Employeedata")
print view.fetchall()

