# Import Flask and required modules
from flask import Flask, redirect, url_for, render_template, request, make_response

# Create a Flask app
app = Flask(__name__)

# Define a route for setting a cookie
@app.route('/cookie')
def cookie():
    # Create a response object with a message
    result = make_response("<h1>cookie is set</h1>")
    # Set a cookie named 'Anshul' with a value of 'Kalia'
    result.set_cookie('Anshul', 'Kalia')
    # Return the response object
    return result;

# Run the Flask app
if __name__ == '__main__':
    app.run(debug = True)


# This code creates a simple Flask app that sets a cookie named "Anshul" with a value of "Kalia" when the user visits the "/cookie" route.