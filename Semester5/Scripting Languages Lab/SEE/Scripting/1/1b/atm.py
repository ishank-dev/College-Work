from flask import Flask, redirect, render_template, request, url_for, session
import time
import re

app = Flask(__name__)
app.secret_key = "secret"  # for pretected routes

@app.route("/", methods=['GET', 'POST'])
def index():
    try:
        balance = session["balance"] # after session has been initialized
        cnt= session["cnt"]
    except KeyError:
        balance = session["balance"] = 8000  # first time only
        cnt=session['cnt']=0

    if request.method == "GET":  # initialize get route,blank msg
        return render_template("index.html", balance=balance, msg="",cnt=cnt)

    if request.method == "POST":
        if request.form["amount"] == "":
            msg = "Amount is required"
            return render_template("index.html", balance=balance, msg=msg,cnt=cnt)

        if int(request.form["amount"]) < 0:
            msg = "Cannot enter negative amount"
            return render_template("index.html", balance=balance, msg=msg,cnt=cnt)

        if request.form["action"] == 'Withdraw':
            if int(request.form["amount"]) > session["balance"]:
                msg = "Cannot withdraw amount greater than balance"
                return render_template("index.html", balance=balance, msg=msg,cnt=cnt)

            elif int(request.form["amount"]) > 5000:
                msg = "Cannot withdraw amount greater than 5000"
                return render_template("index.html", balance=balance, msg=msg,cnt=cnt)

            else:
                if session['cnt'] != 5:
                    balance = balance - int(request.form["amount"])
                    session["balance"] = balance
                    msg = "Money Withdrawn"
                    cnt=cnt+1
                    session['cnt'] = session['cnt'] + 1
                    return render_template("index.html", balance=balance, msg=msg,cnt=cnt)
                else:
                    return render_template("index.html", balance=balance, msg="Max no. of transactions reached", cnt=cnt)

        elif request.form["action"] == 'Deposit':
            if session['cnt'] != 5:
                balance = balance + int(request.form["amount"])
                session["balance"] = balance
                msg = "Money Deposited"
                cnt=cnt+1
                session['cnt']=session['cnt']+1
                return render_template("index.html", balance=balance, msg=msg,cnt=cnt)
            else:
                return render_template("index.html", balance=balance, msg="Max no. of transactions reached", cnt=cnt)

if __name__ == '__main__':
    app.run()