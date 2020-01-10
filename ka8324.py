#! /usr/bin/python3
import cgi
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="proj", password="proj", database="SupplyDB")
mycursor = mydb.cursor()
print("Content-type: text/html\r\n\r\n") 
print("<html><head><meta charset='utf-8'/></head><body>")

form =cgi.FieldStorage()
#part a
if 'pname' in form:
	print("<table align = 'center' border><tr><th>Supplier ID</th><th>Supplier Name</th><th>Supplier Address</th><th>Part Cost</th></tr>")
	name = form['pname'].value
	sql = "SELECT Suppliers.sid, Suppliers.sname, Suppliers.address, Catalog.cost FROM Catalog, Suppliers, Parts WHERE Suppliers.sid = Catalog.sid AND Parts.pid = Catalog.pid AND Parts.pname = " + "'" + name +"'"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print("<tr><td>" + str(x[0]) + "</td><td>" + str(x[1]) + "</td><td>" + str(x[2]) + "</td><td>" + str(x[3]) + "</td></tr>")

#part b
elif 'cost' in form:
	print("<table align = 'center' border><tr><th>Supplier Name</th></tr>")
	cost = form['cost'].value
	sql = "SELECT Suppliers.sname FROM Suppliers, Catalog WHERE Suppliers.sid = Catalog.sid AND Catalog.cost >= " + "'" + cost +"'"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print("<tr><td>" + str(x[0]) + "</td></tr>")

#part c
elif 'pid' in form:
	print("<table align = 'center' border><tr><th>Supplier Name</th><th>Supplier Address</th></tr>")
	pid = form['pid'].value
	sql = "SELECT Suppliers.sname, Suppliers.address FROM Suppliers, Parts, Catalog WHERE Catalog.pid = Parts.pid AND Catalog.sid = Suppliers.sid AND Catalog.cost = (SELECT MAX(Catalog1.cost) FROM Catalog Catalog1 WHERE Catalog1.pid = Parts.pid) AND Parts.pid = " + "'" + pid +"'"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print("<tr><td>" + str(x[0]) + "</td><td>" + str(x[1]) + "</td></tr>")

#part d
elif 'addressE' in form:
	print("<table align = 'center' border><tr><th>Supplier ID</th><th>Supplier Name</th></tr>")
	addressE = form['addressE'].value
	sql = "SELECT Suppliers.sid, Suppliers.sname FROM Suppliers LEFT JOIN Catalog ON Suppliers.sid = Catalog.sid WHERE Catalog.sid IS NULL AND Suppliers.address = " + "'" + addressE +"'"
	mycursor.execute(sql)
	myresult = mycursor.fetchall()
	for x in myresult:
		print("<tr><td>" + str(x[0]) + "</td><td>" + str(x[1]) + "</td></tr>")

#else error
else:
	print("<h2>error go back and enter an input again<h2>")

print("</table>")
print("</body></html>")
