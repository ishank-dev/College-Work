from flask import Flask,request,render_template,url_for,session,redirect

app  = Flask(__name__)

app.secret_key = "secret"

@app.route('/',methods = ["GET","POST"])
def store():
	if request.method == 'GET':
		return render_template('store1.html')
	if request.method == 'POST':
		for item in ['eggs','milk','bread']:
			if item not in session:
				session[item] = int(request.form[item])
			else:
				session[item] += int(request.form[item])
	return redirect(url_for('cart'))
@app.route('/cart',methods = ['GET','POST'])
def cart():
	cart = []
	for item in ['eggs','milk','bread']:
		cart.append({"name":item,"quantity":session[item]})
	return render_template("cart1.html",cart = cart)

if __name__ == ('__main__'):
	app.run(debug = True)
