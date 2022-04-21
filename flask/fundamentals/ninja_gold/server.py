from email import message
from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__) 
app.secret_key = "asdnasdbasd"

def get_gold(range1, range2):
    num = random.randint(range1, range2)
    return num

@app.route('/')          
def hello_world():
    return render_template('index.html', message=message)  

@app.route('/process_money', methods=['POST'])
def money():
    num = 0
    if 'gold' in session:
        pass
    else:
        session['gold'] = 0
        session['message'] = ''
    if request.form['place'] == 'farm':
        num = get_gold(10,20)
        session['message'] += f'<p>You entered the farm at {datetime.datetime.now()}</p>'
        session['message'] += f'<p class="background_green">You got {num} golds.</p>'
        session['gold'] += num
    if request.form['place'] =='cave':
        num = get_gold(5,10)
        session['message'] += f'<p>You entered the cave at {datetime.datetime.now()}</p>'
        session['message'] += f'<p class="background_green">You got {num} golds.</p>'
        session['gold'] += num
    if  request.form['place'] == 'house':
        num = get_gold(2,5)
        session['message'] += f'<p>You entered the house at {datetime.datetime.now()}</p>'
        session['message'] += f'<p class="background_green">You got {num} golds.</p>'
        session['gold'] += num
    if request.form['place'] == 'casino':
        num = get_gold(-50,50)
        session['gold'] += num
        session['message'] += f'<p>You entered the casino at {datetime.datetime.now()}</p>'
        if num > 0:
            session['message'] += f'<p class="background_green">Nice! you got {num} golds. </p>'
        elif num < 0:
            session['message'] += f'<p class="background_red">Unfortunate. You lost {num} golds.</p>'
        else:
            session['message'] += f'<p class="night white">Eh, at least you did not lose gold (+0 golds).</p>'
    
    return redirect('/',)

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

#this needs to stay at the bottom
if __name__=="__main__": 
    app.run(debug=True) 