from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "Naruto"

@app.route('/') 
def options():
    return render_template("Options.html")

@app.route('/login')  
def login():  
    return render_template("Login.html")

@app.route('/valid', methods = ['POST'])
def valid():
    if request.method == "POST":  
        session['email']=request.form['email']
    
    return render_template('Valid.html')

@app.route('/profile')  
def profile():  
    if 'email' in session:  
        email = session['email']
        return render_template('profile.html',name=email) 
    
    else:  
        return '<p>Please add your email address to view your profile.</p>'  

@app.route('/logout')  
def logout():  
    if 'email' in session:  
        session.pop('email', None)  
        return render_template('logout.html');  
    else:  
        return '<p>User already logged out of the session.</p>'  
    
if __name__ == '__main__':  
    app.run(debug = True)  