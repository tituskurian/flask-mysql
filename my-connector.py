import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Kaduva#786',
    port='3306',
    database='mysampledb'
)

employees = []
departments = []
curser = []

try:
    # global employees, departments
    # departments = []
    curser = mydb.cursor()

    curser.execute('SELECT * FROM employee')
    employees =curser.fetchall()
    for employee in employees:
        print(employee)

    curser.execute('SELECT * FROM businesunit')
    departments = curser.fetchall()
except (mysql.connector.errors.InternalError,mysql.connector.errors.ProgrammingError) as e:
    print('SQL error: ',e)
    curser.execute('SELECT * FROM businessunit')
    departments = curser.fetchall()
    for department in departments:
        print(department)
        print('BU: ',department[0])
        print('Zone: ', department[1])
        print('Revenue: ', department[5])
except mysql.connector.errors.ProgrammingError as e:
    print('Query Error:', e)
except NameError as e:
    print('undefined field:', e)
