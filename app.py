from flask import Flask, render_template,request
import mysql.connector
app=Flask(__name__)

@app.route('/')
def bincom_test():
    return render_template('sql-data.html')

@app.route('/adduser')
def adduser():
    return render_template('adduser.html')

@app.route('/submituser',methods=['POST'])
def submituser():
    result_id = request.form['result_id']
    polling_unit_uniqueid  = request.form['polling_unit_uniqueid']
    party_abbreviation = request.form['party_abbreviation']
    party_score = request.form['party_score']
    entered_by_user = request.form['entered_by_user']
    date_entered = request.form['date_entered']
    user_ip_address = request.form['user_ip_address']

    mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Ladenposse3",
  database="bincom"
)

    mycursor = mydb.cursor()
    sql = "INSERT INTO announced_pu_results {result_id},{polling_unit_uniqueid},{party_abbreviation},{party_score},{entered_by_user},{date_entered},{user_ip_address} VALUES "
    val=(result_id,polling_unit_uniqueid,party_abbreviation,party_score,entered_by_user,date_entered,user_ip_address)
    mycursor.execute(sql, val)
    mydb.commit()
    
    return "User added successfully"

if __name__ =='__main__':
    app.run(debug=True)