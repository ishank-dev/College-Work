from flask import Flask, redirect, render_template, request, url_for, session
import time
import re

app = Flask(__name__)

app.secret_key = 'secret'
@app.route('/',methods = ['GET','POST'])
def index():
	try:
		balance = session["balance"]
		count = session["count"]
	except KeyError:
		count = session["count"] = 0
		balance = session["balance"] = 8000

	if request.method == "GET":
		return render_template("atm.html",balance = balance,msg = "Enter the Money",count = count)
	if request.method == "POST":
		if request.form["amount"] == "" :
			msg = "Amount is required"
			return render_template("atm.html",balance = balance,msg = msg)

		if (int(request.form["amount"]<0)):
			msg = "Cannot enter negative amount"
			return render_template("atm.html",balance = balance,msg = msg)


		if session["count"] == 5:
			msg = "5 transcations complete"
			return render_template("atm.html",balance = balance,msg = msg,count = count)

		if request.form["action"] == 'withdraw':
			if(int(request.form["amount"])> session["balance"]):
				msg = "Cannot withdraw amount greater than balance"
				return render_template("atm.html",balance = balance,msg = msg,count = count)
			else:
				balance = balance - int(request.form['amount'])
				session['balance'] = balance
				session["count"] = session["count"]+1
				msg = "Money Withdrawn"
				return render_template("atm.html",balance = balance,msg = msg,count = count)
			
		elif request.form["action"] == "deposit":
			if(int(request.form["amount"])> 5000):
				msg = "Cannot deposit amount greater than 5000"
				return render_template("atm.html",balance = balance,msg = msg,count = count)
			else:
				balance = balance + int(request.form['amount'])
				session['balance'] = balance
				session["count"] = session["count"]+1
				msg = "Amount deposited successfully"
				return render_template("atm.html",balance = balance,msg = msg,count = count)

if __name__ == '__main__':
	app.run(debug = True)
			
