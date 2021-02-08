import sqlite3

def manager_main():
    build = sqlite3.connect('Managers_WS.db')
    connection = build.cursor()
    connection.execute("CREATE TABLE IF NOT EXISTS Managers_WS (id INTEGER PRIMARY KEY, reference text, firstname text, surname text, address text, \
                email_address text, mobile text, IRDnumber text, studentLoan text, tax text, kiwisaver text, deductions text, netpay text, grosspay text)")
    build.commit()
    build.close()

def add_employee_record(reference, firstname,  surname, address, email_address, mobile, IRDnumber, studentLoan, tax, kiwisaver, deductions, netpay, grosspay):
    build = sqlite3.connect('Managers_WS.db')
    connection = build.cursor()
    connection.execute("INSERT INTO Managers_WS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                (reference, firstname, surname, address,  email_address, mobile, IRDnumber, studentLoan, tax, kiwisaver, deductions, netpay, grosspay))
    build.commit()
    build.close()

def view_data():
    build = sqlite3.connect('Managers_WS.db')
    connection = build.cursor()
    connection.execute("SELECT * FROM Managers_WS")
    rows = connection.fetchall()
    build.close()
    return rows

def record_delete(id):
    build = sqlite3.connect('Managers_WS.db')
    connection = build.cursor()
    connection.execute("DELETE * FROM Managers_WS WHERE id=?", (id,))
    build.commit()
    build.close()

def search_records(reference="", firstname="",  surname="", address="", email_address="", mobile="", IRDnumber="", studentLoan="", tax="", kiwisaver="", deductions="", netpay="", grosspay=""):
    build = sqlite3.connect('Managers_WS.db')
    connection = build.cursor()
    connection.execute("SELECT * FROM Managers_WS WHERE reference="" OR firstname="" OR surname="" OR address="" OR email_address="" OR mobile="" OR IRDnumber=""\
                        OR studentLoan="" OR tax="" OR kiwisaver=""\ OR  deductions="" OR netpay="" OR grosspay=", \
                (reference, firstname,  surname, address, email_address, mobile, IRDnumber, studentLoan, tax, kiwisaver, deductions, netpay, grosspay))
    rows = connection.fetchall()
    build.close()
    return rows

def update_records(reference="", firstname="",  surname="", address="", email_address="", mobile="", IRDnumber="", studentLoan="", tax="", kiwisaver="", deductions="", netpay="", grosspay=""):
    build = sqlite3.connect('Managers_WS.db')
    connection = build.cursor()
    build.execute("UPDATE Managers_WS SET reference="", firstname="",  surname="", address="",  gender="", mobile="",  IRDnumber="",  studentLoan="",  tax="",  kiwisaver="",  deductions="", netpay="",  grosspay=", \
                (reference, firstname,  surname, address, email_address, mobile, IRDnumber, studentLoan, tax, kiwisaver, deductions, netpay, grosspay, id))
    build.commit()
    build.close()

manager_main()



