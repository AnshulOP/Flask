# Importing the necessary modules from the Flask package
from flask import Flask, redirect, url_for, render_template, request

# Creating a Flask app instance
app = Flask(__name__)

# Defining a route for the homepage
@app.route('/')
def welcome():
    # Rendering an HTML template called Integrating_HTML.html using Flask's render_template method
    return render_template('Integrating_HTML.html')

# Defining a route to display a message for high-level repository creators
@app.route('/high/<int:number>')
def high(number):
    # Creating a string variable called 'result' to store the result message for high-level creators
    result = "You are a high level repository creator with total number of repositories equal to " + str(number) + ", you have crossed " + str(number - 4) + " repositories more than a low level creator."
    # Rendering an HTML template called result.html using Flask's render_template method, and passing in the 'result' variable to display the result message
    return render_template('result.html', result=result)

# Defining a route to display a message for low-level repository creators
@app.route('/low/<int:number>')
def low(number):
    # Creating a string variable called 'result' to store the result message for low-level creators
    result = "You are a low level repository creator with total number of repositories equal to " + str(number) + ", create " + str(5 - number) + " more repositories to become a high level creator."
    # Rendering an HTML template called result.html using Flask's render_template method, and passing in the 'result' variable to display the result message
    return render_template('result.html', result=result)

# Defining a route for the form submission to calculate the total number of repositories
@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    # Initializing a variable to store the total number of repositories
    total_repositories = 0
    # Checking if the form was submitted with the POST method
    if request.method == 'POST':
        # Retrieving the values of the form fields and converting them to integers
        java = int(request.form['java'])
        flask = int(request.form['flask'])
        jupyter = int(request.form['jupyter'])
        python = int(request.form['python'])
        mysql = int(request.form['mysql'])
        # Calculating the total number of repositories
        total_repositories = java + flask + jupyter + python + mysql
    # Initializing a variable to store the result message
    result = ''
    # Checking if the total number of repositories is greater than or equal to 5
    if total_repositories >= 5:
        # Setting the result variable to 'high' if the total number of repositories is greater than or equal to 5
        result = 'high'
    else:
        # Setting the result variable to 'low' if the total number of repositories is less than 5
        result = 'low'
    # Redirecting the user to the appropriate route based on their total number of repositories
    return redirect(url_for(result, number=total_repositories))

# Running the app if it is the main module
if __name__ == '__main__':
    # Starting the app in debug mode
    app.run(debug=True)
