# Importing the necessary modules from the Flask package
from flask import Flask, redirect, url_for, render_template, request

# Creating a Flask app instance
app = Flask(__name__)
app.static_folder = 'static'

# Defining a route for the homepage
@app.route('/')
def welcome():
    # Render the 'Integrating_CSS_Javascript.html' template
    return render_template('Integrating_CSS_Javascript.html')

# @app.route('/repositories/<int:number>')
# def repositories(number):
#     return render_template('Templates.html', result = number)

# Defining a route for the 'repositories' page with the number of repositories as a parameter
@app.route('/repositories/<int:number>')
def repositories(number):
    # Determine the repository level based on the number of repositories
    result = ""
    if number >= 5:
        result = "High Level"
    else:
        result = "Low Level"
    # Create a dictionary with the repository information
    dictionary = {'Repositories': number, 'Level': result}
    # Render the 'Templates.html' template with the dictionary as a parameter
    return render_template('Templates.html', result=dictionary)


# Defining a route for the 'calculate' page with the ability to receive POST and GET requests
@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    # Initialize the total number of repositories to 0
    total_repositories = 0
    # If a POST request is received
    if request.method == 'POST':
        # Retrieve the number of repositories for each programming language from the form data
        java = int(request.form['java'])
        flask = int(request.form['flask'])
        jupyter = int(request.form['jupyter'])
        python = int(request.form['python'])
        mysql = int(request.form['mysql'])
        shell = int(request.form['shell'])

        # Calculate the total number of repositories
        total_repositories = java + flask + jupyter + python + mysql + shell

    # Set the result to the 'repositories' page with the total number of repositories as a parameter
    result = 'repositories'
    return redirect(url_for(result, number=total_repositories))


# Running the app if it is the main module
if __name__ == '__main__':
    # Starting the app in debug mode
    app.run(debug=True)
