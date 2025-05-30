import pandas as pd
import MySQLdb
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='templates')

# MySQL Configuration
app.config['MYSQL_HOST'] = "host.docker.internal"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "mysampledb"

myFlaskSql = MySQL(app)

cursor = []
busql = "INSERT INTO businessunit(BuCode,Name,Head,EmpCount,ProjectCount,Revenue) VALUES (%s,%s,%s,%s,%s,%s)"
buselect = "SELECT * FROM businessunit"
budetails = []

def get_db_connect():
    return myFlaskSql.connection

@app.route("/", methods=['GET', 'POST'])
def home():
    # return "Hailo World"
    if request.method == 'POST':
        empid = request.form['empid']
        empname = request.form['empname']

        cursor = get_db_connect().cursor()
        try:
            buval = (empid, empname, ' ', 3, 3, 7000000.00)
            cursor.execute(busql,buval)
        except MySQLdb.ProgrammingError as e:
            return "failure: " + e.__str__()
        finally:
            myFlaskSql.connection.commit()
        return "success"
    return render_template('home.html')

@app.route("/bu")
def bu():
    cursor = get_db_connect().cursor()
    bus = cursor.execute(buselect)
    if bus > 0:
        budetails = cursor.fetchall()
        return render_template('bus.html',budetails=budetails)

@app.route("/business")
def business():
    con = get_db_connect()
    df = pd.read_sql(buselect, con)
    response = df.to_json(orient="records")
    # response = df.to_json(budetails)
    return response

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')