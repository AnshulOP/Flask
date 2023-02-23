# Importing Flask and redirect and url_for modules from Flask module
from flask import Flask
from flask import redirect
from flask import url_for

# Creating a Flask app instance
app = Flask(__name__)

# Defining a route for the homepage
@app.route('/')
def welcome():
    # Returns a welcome message to the user
    return "Welcome to my Github, you will learn more about Flask here"

# Defining a route to display a message for high-level repository creators
@app.route('/high/<int:number>')
def high(number):
    # Returns a message to the user with the number of repositories passed as a parameter
    return "You are a high level repository creator with total number of repositories equal to " + str(number)

# Defining a route to display a message for low-level repository creators
@app.route('/low/<int:number>')
def low(number):
    # Returns a message to the user with the number of repositories passed as a parameter
    return "You are a low level repository creator with total number of repositories equal to " + str(number)

# Defining a route to redirect the user to either the high-level or low-level repository route based on the number of repositories
@app.route('/results/<int:repositories>')
def results(repositories):
    # Initializing an empty string to store the result
    result = ""
    # Checking the number of repositories and assigning the result accordingly
    if repositories >= 5:
        result = 'high'
    elif repositories < 5:
        result = 'low'
    # Redirecting the user to either the high-level or low-level repository route based on the result
    return redirect(url_for(result, number=repositories))

# Defining a route to display information about a user's name and age
@app.route('/information/<string:name>/<int:age>')
def information(name, age):
    # Returns a message to the user with their name and age passed as parameters
    return f"Hello {name}, your Age is {age}"


# Running the app if it is the main module
if __name__ == '__main__':
    # Starting the app in debug mode
    app.run(debug=True)
