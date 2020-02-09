from flask import Flask, redirect,render_template,session,request

app=Flask(__name__)
app.secret_key="secret"

@app.route('/',methods=['POST','GET'])
def index():
    try:
        amt=session['amt']
    except KeyError:
        amt=session['amt']=0

    if request.method=='GET':
        return render_template('mart.html',msg="")

    elif request.method=='POST':
        if request.form['egg']=="" or request.form['mil']=="" or request.form['bre']=="":
            return render_template('mart.html', msg="Empty quantity fields")

        if int(request.form['egg'])<0 or int(request.form['mil'])<0 or int(request.form['bre'])<0:
            return render_template('mart.html', msg="Invalid Entry")
        else:
            amt = amt + int(request.form['egg'])*3 + int(request.form['mil'])*20 + int(request.form['bre'])*40
            session['amt']=amt
            return render_template('mart.html',msg='Total amt=Rs.'+str(session['amt']))

if __name__ == '__main__':
    app.run()