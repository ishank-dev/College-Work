from flask import Flask,redirect,render_template,url_for,request
import re
import time

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=="GET":
        return render_template('student.html',msg="")

    elif request.method=="POST":
        if request.form['usn']=="" or request.form['dob']=="" or request.form['m1']=="" or request.form['m2']=="" or request.form['m3']=="":
            return render_template('student.html',msg="Empty fields entered")
        elif int(request.form['m1'])<0 or int(request.form['m2'])<0 or int(request.form['m3'])<0:
            return  render_template('student.html',msg="Invalid marks obtained")
        else:
            try:
                time.strptime(request.form["dob"], "%d/%m/%Y")
            except ValueError:
                return render_template("student.html", msg="Date is invalid")

            if re.match('^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$', request.form["usn"]):
                avg = (int(request.form['m1'])+int(request.form['m2'])+int(request.form['m3']))/3.0
                return render_template('student.html',msg="Avg="+str(avg))
            else:
                return render_template('student.html',msg="Invalid USN")


if __name__=='__main__':
    app.run()
