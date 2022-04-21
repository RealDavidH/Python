from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = 'key key key'
fruits_list = [
    'apple.png',
    'blackberry.png',
    'raspberry.png',
    'strawberry.png'
]

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fruits_total = int(request.form['apple'] + request.form['raspberry'] + request.form['strawberry'])
    name = f"{request.form['first_name']} {request.form['last_name']}"
    # session['amount_strawberry'] = 
    # session['amount_raspberry'] = 
    # session['amount_apple'] = 
    # print(session)
    return render_template("checkout.html", amount=fruits_total, customer_name=name)

@app.route('/fruits')         
def fruits():
    print(fruits_list)
    return render_template("fruits.html", fruit=fruits_list)

if __name__=="__main__":   
    app.run(debug=True)    