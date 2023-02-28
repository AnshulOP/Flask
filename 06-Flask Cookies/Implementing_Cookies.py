# Import Flask and required modules
from flask import Flask, redirect, url_for, render_template, request, make_response

# Create a Flask app
app = Flask(__name__)

# Define a route for displaying the login page
@app.route('/')
def details():
    # Render the Login.html template
    return render_template('Login.html')

# Define a route for handling form submission and setting a cookie
@app.route('/valid', methods = ['POST'])
def valid():
    # Check if the request method is POST
    if request.method == 'POST':
        # Get the values of the email and password fields from the submitted form
        email = request.form['email']
        password = request.form['password']
    
    # Check if the password is correct
    if password == "Github":
        # If the password is correct, create a response object with the Valid.html template
        done = make_response(render_template('Valid.html'))
        # Set a cookie named 'email' with the value of the submitted email
        done.set_cookie('email', email)
        # Return the response object
        return done
    else:
        # If the password is incorrect, redirect the user to the 'error' route
        return redirect(url_for('error'))

# Define a route for displaying an error message
@app.route('/error')
def error():
    # Return an HTML response containing a JavaScript alert box with an error message
    return "<script>alert('Wrong Password, Please go back and enter correct password')</script>"

# Define a route for displaying the user's profile
@app.route('/profile')
def profile():
    # Get the value of the 'email' cookie
    email = request.cookies.get('email')
    # Create a response object with the Profile.html template and the user's email address
    result = make_response(render_template('Profile.html', name = email))
    # Return the response object
    return result

# Run the Flask app in debug mode
if __name__ == "__main__":  
    app.run(debug = True)


# This code creates a simple Flask app that allows the user to enter their email address and password in a form, and then sets a cookie with their email address if the correct password is entered.
# Next, a Flask app is created and routes are defined for displaying the login page, handling form submission and setting a cookie, displaying an error message, and displaying the user's profile.

# When the user submits the form, the valid() function is called with the HTTP method of POST. If the correct password is entered, a response object is created with the Valid.html template and a cookie named "email" is set with the value of the submitted email address. If the password is incorrect, the user is redirected to the "error" route, which displays an HTML response containing a JavaScript alert box with an error message.

# When the user visits the "profile" route, the profile() function is called and the value of the "email" cookie is retrieved using the request.cookies.get() method. A response object is then created with the Profile.html template and the user's email address.