from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('stud.html')
	if request.method == 'POST':
		total = int(request.form['marks1']) + int(request.form['marks2']) + int(request.form['marks3'])
		per = total/3
		return render_template('stud.html',msg = "Total marks percentage obtained is" + str(per))

if __name__ == '__main__':
	app.run(debug  = True)
